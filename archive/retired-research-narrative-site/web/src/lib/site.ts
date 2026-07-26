const origin = (
  import.meta.env.PUBLIC_SITE_ORIGIN ||
  "https://human-infra.pages.dev"
).replace(/\/$/, "");
const basePath = (import.meta.env.BASE_URL || "/").replace(/^\/$/, "").replace(/\/$/, "");

export const SITE = {
  name: "Human Infra",
  alternateName: "人类基础设施",
  publisher: "tradecatlabs",
  language: ["zh-CN", "en"],
  origin,
  basePath,
  publicUrl: `${origin}${basePath}/`,
  repository: "https://github.com/tradecatlabs/human_infra",
  community: "https://t.me/human_infra",
  license: "https://github.com/tradecatlabs/human_infra/blob/main/LICENSE.md",
  description:
    "Human Infra is an evidence-governed research knowledge base for engineering subject continuity: the conditions that let a human continue to exist, act, learn, recover, choose, and reach the future.",
  definition:
    "Human Infra 研究如何工程化维护、延展和升级能够继续存在、行动、学习、恢复、选择并进入未来的主体。",
  lastReviewed: "2026-07-14"
} as const;

export const TIER_DEFINITIONS = [
  {
    id: "C1",
    slug: "boundary-rewriting",
    name: "可能性边界改写层",
    shortName: "边界改写",
    question: "能否改写寿命、死亡、时间、身份连续性与未来抵达边界？"
  },
  {
    id: "C2",
    slug: "source-maintenance",
    name: "可能性源体维护层",
    shortName: "源体维护",
    question: "能否维护产生可能性的身体、脑与生命系统？"
  },
  {
    id: "C3",
    slug: "generation-engine",
    name: "可能性生成引擎层",
    shortName: "生成引擎",
    question: "能否增强认知、学习、注意力、AI 协作与新路径生成？"
  },
  {
    id: "C4",
    slug: "conversion-channel",
    name: "可能性转换通道层",
    shortName: "转换通道",
    question: "能否把知识、技术、权利和服务转换为可执行路径？"
  },
  {
    id: "C5",
    slug: "ecological-substrate",
    name: "可能性生态承载层",
    shortName: "生态承载",
    question: "能否提供行动所需的资源、环境、制度与基础设施？"
  },
  {
    id: "C6",
    slug: "local-unlocking",
    name: "局部可能性解锁层",
    shortName: "局部解锁",
    question: "能否解除具体任务、流程和生活中的最后一公里阻塞？"
  }
] as const;

export const PUBLIC_PAGES = [
  {
    route: "/",
    title: "Human Infra × 奇点更近",
    description: "主体持续性研究、生命路径模型与技术窗口的科研叙事入口。",
    type: "CollectionPage",
    topics: ["主体持续性", "生命路径", "Human Infra"]
  },
  {
    route: "/about/",
    title: "关于 Human Infra",
    description: "Human Infra 的规范定义、研究对象、方法、边界、作者与机器入口。",
    type: "AboutPage",
    topics: ["项目定义", "研究边界", "tradecatlabs"]
  },
  {
    route: "/research-map/",
    title: "研究域地图",
    description: "按可能性空间控制力组织的 C1-C6 研究域公开索引。",
    type: "CollectionPage",
    topics: ["C1-C6", "研究域", "实体图谱"]
  },
  {
    route: "/evidence-map/",
    title: "Human Infra 证据图",
    description: "连接优先研究域主张、来源锚点、反证条件、候选端点和迁移边界的证据地图。",
    type: "Dataset",
    topics: ["证据图", "Source Card", "反证条件", "Fact Card"]
  },
  {
    route: "/paper/",
    title: "Human Infra 主论文",
    description: "主体持续性基础设施、生命路径建模与科研可视化主论文。",
    type: "ScholarlyArticle",
    topics: ["主体持续性", "生命路径模型", "研究协议"]
  },
  {
    route: "/papers/effective-immortality-flywheel/",
    title: "有效永生与主体持续性加速回报飞轮",
    description: "有效永生、学习轮次、技术采用与可能性空间之间的递归增强模型。",
    type: "ScholarlyArticle",
    topics: ["有效永生", "加速回报", "主体持续性"]
  },
  {
    route: "/papers/metric-redshift-recursive-waiting/",
    title: "度规红移递归等待假设",
    description: "用固有时差分等待外部技术窗口的条件性研究协议。",
    type: "ScholarlyArticle",
    topics: ["固有时", "度规红移", "未来等待"]
  },
  {
    route: "/papers/proper-time-differential-waiting-hypothesis/",
    title: "度规红移固有时差分等待假设",
    description: "强红移环境、固有时差分、退出可达性与主体连续性的研究框架。",
    type: "ScholarlyArticle",
    topics: ["广义相对论", "固有时差分", "主体连续性"]
  },
  {
    route: "/papers/controllable-metric-waiting-room-hypothesis/",
    title: "可控度规等待室假设",
    description: "等待、退出、采用技术和再等待的递归未来访问假设。",
    type: "ScholarlyArticle",
    topics: ["可控度规", "未来访问", "递归等待"]
  },
  {
    route: "/book/",
    title: "《奇点更近》研究转译",
    description: "把书内技术叙事转译为 Human Infra 变量、因果链和证据边界。",
    type: "Article",
    topics: ["奇点更近", "技术趋势", "学习资料"]
  },
  {
    route: "/model/",
    title: "生命路径预测模型",
    description: "寿命、有效时间、主观时间、相对时间和未来选择权的合成模型展示。",
    type: "WebApplication",
    topics: ["生存分析", "生命路径", "预测模型"]
  },
  {
    route: "/lev/",
    title: "长寿逃逸速度路线",
    description: "直接与间接影响长寿逃逸速度的研究路线、概率门和多阶效应。",
    type: "Article",
    topics: ["长寿逃逸速度", "干预路线", "多阶效应"]
  },
  {
    route: "/research-standards/",
    title: "科研标准",
    description: "Human Infra 的证据、偏倚、报告、模型透明度与引用边界。",
    type: "TechArticle",
    topics: ["证据治理", "科研标准", "Source Card"]
  }
] as const;

export function normalizeRoute(path: string): string {
  const withoutBase = path.startsWith(SITE.basePath) ? path.slice(SITE.basePath.length) : path;
  const normalized = `/${withoutBase.replace(/^\/+|\/+$/g, "")}`;
  if (normalized === "/") return "/";

  // GitHub Pages 将带扩展名的端点和资源发布为文件，页面路由才使用尾斜杠。
  return /\/[^/]+\.[^/]+$/.test(normalized) ? normalized : `${normalized}/`;
}

export function withBase(path: string): string {
  const route = normalizeRoute(path);
  const runtimeBase = (import.meta.env.BASE_URL || "/").replace(/\/$/, "");
  return runtimeBase ? `${runtimeBase}${route}` : route;
}

export function publicUrl(path = "/"): string {
  return new URL(`${SITE.basePath}${normalizeRoute(path)}`, SITE.origin).href;
}

export function githubPath(path: string): string {
  return `${SITE.repository}/blob/main/${path.replace(/^\//, "")}`;
}

export function resolvePublishedHref(href: string): string {
  if (/^(?:https?:|mailto:|#)/.test(href)) return href;
  if (/^\/?(?:docs|domains|tools)\//.test(href)) return githubPath(href);
  if (href.startsWith("/")) return withBase(href);
  return href;
}
