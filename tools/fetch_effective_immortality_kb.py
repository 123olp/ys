#!/usr/bin/env python3
"""有效永生知识库采集器：PubMed 检索 -> 元数据 -> 开放获取检查。

用法:
  python3 tools/fetch_effective_immortality_kb.py --batch A1
  python3 tools/fetch_effective_immortality_kb.py --batch all

输出:
  .research/literature/effective-immortality-kb/metadata/<batch>.json
  .research/literature/effective-immortality-kb/manifest.json
"""
import argparse
import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

BASE = Path(".research/literature/effective-immortality-kb")
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest"

BATCHES = {
    "A1": {
        "label": "衰老机制",
        "category": "aging-mechanism",
        "queries": {
            "hallmarks_of_aging": 'hallmarks of aging[Title] AND review[Publication Type]',
            "cellular_senescence_review": 'cellular senescence[Title] AND aging AND review[Publication Type]',
            "mitochondrial_aging": 'mitochondria[Title] AND aging AND review[Publication Type]',
            "proteostasis_aging": 'proteostasis[Title] AND aging AND review[Publication Type]',
            "telomere_aging_review": 'telomere[Title] AND aging AND review[Publication Type]',
            "autophagy_aging": 'autophagy[Title] AND aging AND review[Publication Type]',
            "stem_cell_aging": 'stem cell[Title] AND aging AND review[Publication Type]',
            "epigenetic_aging": 'epigenetic[Title] AND aging AND review[Publication Type]',
            "dna_damage_aging": 'DNA damage[Title] AND aging AND review[Publication Type]',
            "inflammaging": 'inflammaging[Title] AND review[Publication Type]',
            "sarcopenia_mechanism": 'sarcopenia[Title] AND mechanism AND review[Publication Type]',
            "glycation_aging": 'glycation[Title] AND aging AND review[Publication Type]',
        },
        "retmax": 3,
    },
    "A2": {
        "label": "长寿干预",
        "category": "intervention",
        "queries": {
            "caloric_restriction_human": 'caloric restriction[Title] AND human AND randomized',
            "senolytics_review": 'senolytics[Title] AND review',
            "nad_precursor_human": '(NMN OR nicotinamide riboside) AND human trial',
            "epigenetic_reprogramming": 'epigenetic reprogramming AND aging AND (Yamanaka OR partial)',
            "geroprotector_review": 'geroprotector AND longevity AND review',
            "metformin_aging": 'metformin[Title] AND aging AND (trial OR review)',
            "mTOR_inhibition": 'mTOR inhibition[Title] AND aging AND review',
            "young_blood": 'young blood OR heterochronic parabiosis AND aging AND review',
            "gene_therapy_aging": 'gene therapy AND aging AND review[Publication Type]',
            "organ_transplant_review": 'organ transplantation[Title] AND review[Publication Type]',
            "xenotransplantation_review": 'xenotransplantation[Title] AND review[Publication Type]',
            "senescent_cell_clearance_human": 'senolytics AND human AND clinical trial',
        },
        "retmax": 3,
    },
    "A3": {
        "label": "健康证据",
        "category": "health-evidence",
        "queries": {
            "physical_activity_mortality": 'physical activity[Title] AND all-cause mortality AND meta-analysis',
            "resistance_training_sarcopenia": 'resistance training AND sarcopenia AND meta-analysis',
            "sleep_duration_mortality": 'sleep duration[Title] AND mortality AND meta-analysis',
            "mediterranean_diet": 'mediterranean diet[Title] AND meta-analysis AND mortality',
            "vitamin_d_review": 'vitamin D supplementation AND randomized AND systematic review',
            "omega3_cardio": 'omega-3 fatty acids AND cardiovascular AND meta-analysis',
            "loneliness_mortality": 'loneliness AND social isolation AND mortality AND meta-analysis',
            "protein_intake_elderly": 'protein intake[Title] AND (older adults OR elderly) AND meta-analysis',
            "time_restricted_eating": 'time-restricted eating AND randomized AND human',
            "blood_pressure_control": 'blood pressure control[Title] AND mortality AND meta-analysis',
            "cancer_screening_review": 'cancer screening[Title] AND (colorectal OR breast OR lung) AND systematic review',
            "smoking_cessation_mortality": 'smoking cessation AND mortality AND meta-analysis',
            "mediterranean_cognitive": 'mediterranean diet AND cognition AND cohort',
            "vitamin_b12_elderly": 'vitamin B12[Title] AND older adults AND deficiency',
            "creatine_sarcopenia": 'creatine[Title] AND (sarcopenia OR muscle strength) AND meta-analysis',
        },
        "retmax": 3,
    },
    "A4": {
        "label": "数字路径",
        "category": "digital-path",
        "queries": {
            "whole_brain_emulation": 'whole brain emulation[Title] OR mind uploading[Title]',
            "brain_preservation_connectome": 'connectome[Title] AND (preservation OR reconstruction)',
            "mouse_connectome": 'whole brain connectome[Title] AND mouse',
            "consciousness_ncc": 'neural correlates of consciousness[Title] AND review',
            "consciousness_integrated": 'integrated information theory[Title] AND consciousness',
            "brain_computer_interface": 'brain-computer interface[Title] AND review[Publication Type] AND 2019:2026[dp]',
            "neuromorphic_computing": 'neuromorphic computing[Title] AND review[Publication Type]',
            "organoid_intelligence": 'organoid intelligence[Title] OR dishbrain',
            "memory_engram": 'memory engram[Title] AND review',
        },
        "retmax": 3,
    },
    "A5": {
        "label": "哲学判据",
        "category": "philosophy",
        "queries": {
            "personal_identity_review": 'personal identity[Title] AND review',
            "narrative_identity": 'narrative identity[Title] AND (self OR psychology)',
            "death_philosophy": 'philosophy of death[Title]',
            "temporal_experience": 'time consciousness[Title] AND philosophy',
            "self_continuity": 'self-continuity[Title] AND (psychology OR neuroscience)',
        },
        "retmax": 3,
    },
    "A6": {
        "label": "历史思想",
        "category": "history-ideas",
        "queries": {
            "transhumanism_history": 'transhumanism[Title] AND review',
            "cryonics_ethics": 'cryonics[Title] AND (ethics OR review)',
            "immortality_history": 'immortality[Title] AND history',
            "longevity_movement": 'longevity[Title] AND movement AND society',
        },
        "retmax": 3,
    },
    "A7": {
        "label": "认知外延",
        "category": "cognitive-augmentation",
        "queries": {
            "cognitive_augmentation": 'cognitive augmentation[Title] AND review',
            "extended_mind": 'extended mind[Title] AND (Clark OR cognition)',
            "cognitive_training_meta": 'cognitive training[Title] AND meta-analysis AND older adults',
            "lifelong_learning_brain": 'lifelong learning[Title] AND (brain OR cognition)',
            "ai_productivity_work": 'artificial intelligence AND productivity AND workers',
            "memory_aids_external": 'prospective memory[Title] AND (external OR reminder) AND older adults',
            "bilingual_cognitive_reserve": 'cognitive reserve[Title] AND dementia AND review',
        },
        "retmax": 3,
    },
    "A8": {
        "label": "社会复合",
        "category": "social-substrate",
        "queries": {
            "social_capital_health": 'social capital[Title] AND health AND review',
            "social_prescribing": 'social prescribing[Title] AND (health OR wellbeing) AND review',
            "financial_stress_health": 'financial stress[Title] AND health AND mortality',
            "volunteering_mortality": 'volunteering[Title] AND mortality AND older',
            "marriage_health_longevity": 'marriage[Title] AND mortality AND meta-analysis',
            "social_support_intervention": 'social support intervention[Title] AND older adults AND review',
        },
        "retmax": 3,
    },
    "A9": {
        "label": "生物重建",
        "category": "bio-reconstruction",
        "queries": {
            "regenerative_medicine_review": 'regenerative medicine[Title] AND review[Publication Type]',
            "tissue_engineering_review": 'tissue engineering[Title] AND review[Publication Type]',
            "bioprinting_organ": 'bioprinting[Title] AND organ AND review',
            "ipsc_therapy": 'iPSC[Title] AND (cell therapy OR clinical) AND review',
            "stem_cell_aging_tissue": 'stem cell therapy[Title] AND aging AND review',
            "organ_perfusion_preservation": 'organ perfusion[Title] AND preservation AND review',
            "3d_printed_tissues": '3D bioprinting[Title] AND vascularized',
        },
        "retmax": 3,
    },
    "A10": {
        "label": "生物暂停",
        "category": "biostasis",
        "queries": {
            "cryopreservation_review": 'cryopreservation[Title] AND review[Publication Type]',
            "organ_cryopreservation": 'organ cryopreservation[Title] OR vitrification[Title] AND organ',
            "hibernation_science": 'hibernation[Title] AND (mammal OR human) AND review',
            "suspended_animation": 'suspended animation[Title] AND review',
            "anhydrobiosis": 'anhydrobiosis[Title] AND (tardigrade OR mechanism)',
            "cryoprotectant_advances": 'cryoprotectant[Title] AND (new OR novel) AND (tissue OR organ)',
        },
        "retmax": 3,
    },
    "A11": {
        "label": "营养补剂",
        "category": "supplements",
        "queries": {
            "vitamin_d_meta": 'vitamin D[Title] AND supplementation AND meta-analysis AND mortality',
            "magnesium_supplement": 'magnesium[Title] AND supplementation AND (sleep OR blood pressure) AND meta-analysis',
            "omega3_meta_mortality": 'omega-3[Title] AND all-cause mortality AND meta-analysis',
            "probiotics_review": 'probiotics[Title] AND (gut OR immune) AND review',
            "protein_supplement_muscle": 'protein supplementation[Title] AND muscle AND older adults AND meta-analysis',
            "multivitamin_cognition": 'multivitamin[Title] AND cognition AND randomized',
            "vitamin_b12_neuro": 'vitamin B12[Title] AND (cognitive OR neuropathy) AND review',
            "polyphenol_aging": 'polyphenols[Title] AND aging AND review',
        },
        "retmax": 3,
    },
    "A12": {
        "label": "筛查疫苗",
        "category": "screening-vaccine",
        "queries": {
            "colorectal_screening_effect": 'colorectal cancer screening[Title] AND (mortality OR effectiveness) AND randomized',
            "lung_screening_ldct": 'low-dose CT[Title] AND lung cancer AND mortality AND randomized',
            "breast_screening_overview": 'breast cancer screening[Title] AND mortality AND randomized AND review',
            "vaccines_older_adults": 'vaccination[Title] AND older adults AND (effectiveness OR mortality) AND review',
            "shingles_vaccine": 'shingles vaccine[Title] AND older adults AND effectiveness',
            "annual_checkup_effect": 'general health check[Title] AND mortality AND randomized',
            "aging_biomarkers_clinical": 'aging biomarker[Title] AND clinical AND (validation OR use)',
        },
        "retmax": 3,
    },
    "A13": {
        "label": "临床前沿",
        "category": "clinical-frontier",
        "queries": {
            "rapamycin_clinical": 'rapamycin[Title] AND (human OR clinical) AND aging',
            "metformin_tame": 'metformin AND aging AND (TAME OR trial)',
            "senolytics_clinical_trial": 'senolytics AND clinical trial AND human',
            "longevity_medicine_clinic": 'longevity medicine[Title] AND (clinic OR practice) AND review',
            "geroscience_trials": 'geroscience[Title] AND clinical trial AND review',
            "epigenetic_clock_intervention": 'epigenetic clock[Title] AND intervention AND (randomized OR trial)',
        },
        "retmax": 3,
    },
    "A14": {
        "label": "经济制度",
        "category": "economy-institution",
        "queries": {
            "aging_economics": 'aging[Title] AND economics AND (review OR burden) AND 2020:2026[dp]',
            "longevity_economy": 'longevity economy[Title]',
            "social_protection_aging": 'social protection[Title] AND older adults AND review',
            "long_term_care_financing": 'long-term care[Title] AND financing AND review',
            "retirement_health": 'retirement[Title] AND health AND longitudinal',
        },
        "retmax": 3,
    },
}


def http_get_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "human-infra-kb/0.1"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


def esearch(query: str, retmax: int) -> list[str]:
    url = f"{EUTILS}/esearch.fcgi?db=pubmed&term={urllib.parse.quote(query)}&retmax={retmax}&retmode=json"
    data = http_get_json(url)
    return data["esearchresult"].get("idlist", [])


def esummary(pmids: list[str]) -> dict:
    if not pmids:
        return {}
    url = f"{EUTILS}/esummary.fcgi?db=pubmed&id={','.join(pmids)}&retmode=json"
    data = http_get_json(url)
    return data.get("result", {})


def epmc_open_access(pmids: list[str]) -> dict[str, dict]:
    """用 Europe PMC 批量查询 PMCID 与开放获取状态。"""
    if not pmids:
        return {}
    out: dict[str, dict] = {}
    for i in range(0, len(pmids), 20):
        chunk = pmids[i : i + 20]
        q = " OR ".join(f"EXT_ID:{p}" for p in chunk)
        url = f"{EPMC}/search?query={urllib.parse.quote('(' + q + ') AND SRC:MED')}&format=json&pageSize=100"
        try:
            data = http_get_json(url)
            for hit in data.get("resultList", {}).get("result", []):
                out[hit.get("pmid")] = {
                    "pmcid": hit.get("pmcid", ""),
                    "isOpenAccess": hit.get("isOpenAccess") == "Y",
                    "inPMC": hit.get("inPMC") == "Y",
                    "doi": hit.get("doi", ""),
                }
        except Exception as exc:  # noqa: BLE001
            print(f"  epmc error chunk: {exc}")
        time.sleep(0.4)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", default="all", help="A1|A2|A3|A4|all")
    args = ap.parse_args()

    meta_dir = BASE / "metadata"
    meta_dir.mkdir(parents=True, exist_ok=True)

    manifest_path = BASE / "manifest.json"
    manifest: dict = json.loads(manifest_path.read_text()) if manifest_path.exists() else {"batches": {}}

    batches = BATCHES if args.batch == "all" else {args.batch: BATCHES[args.batch]}
    for bid, spec in batches.items():
        print(f"\n=== 批次 {bid}: {spec['label']} ===")
        rows: list[dict] = []
        for qname, query in spec["queries"].items():
            print(f"  [检索] {qname}: {query}")
            pmids = esearch(query, spec["retmax"])
            print(f"    -> {len(pmids)} 条: {pmids}")
            if not pmids:
                continue
            summ = esummary(pmids)
            oa = epmc_open_access(pmids)
            for pid in pmids:
                s = summ.get(pid, {})
                row = {
                    "query": qname,
                    "pmid": pid,
                    "pmcid": oa.get(pid, {}).get("pmcid", ""),
                    "open_access": oa.get(pid, {}).get("isOpenAccess", False),
                    "doi": oa.get(pid, {}).get("doi", "") or s.get("elocationid", "").replace("doi: ", ""),
                    "title": s.get("title", ""),
                    "year": s.get("pubdate", ""),
                    "journal": s.get("fulljournalname", ""),
                    "source": s.get("source", ""),
                    "status": "oa-downloadable" if oa.get(pid, {}).get("isOpenAccess") else "metadata-only",
                }
                rows.append(row)
                print(f"    + {row['pmid']} [{row['status']}] {row['title'][:60]}")
            time.sleep(0.4)

        out_path = meta_dir / f"{bid}.json"
        out_path.write_text(json.dumps(rows, ensure_ascii=False, indent=2))
        manifest["batches"][bid] = {
            "label": spec["label"],
            "category": spec["category"],
            "count": len(rows),
            "open_access": sum(1 for r in rows if r["open_access"]),
            "metadata_file": str(out_path.relative_to(BASE)),
        }
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2))
        print(f"  [完成] {len(rows)} 条 -> {out_path.name}")


if __name__ == "__main__":
    main()
