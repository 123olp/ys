# Pages smoke 相对资源路径拼接失败

## Bug

- 标题：科技树相对 chunk 路径被直接拼接到域名
- 症状：`make pages-smoke` 请求
  `https://tree.tradecatlabs.com_next/...` 并以 `curl` 退出码 35 失败
- 影响：生产站点实际可用，但发布后的综合 smoke 被错误阻塞

## Environment

- 模块：`scripts/smoke-pages-release.sh`
- 输入：科技树首页中的相对资源路径 `_next/static/...`
- 入口：`https://tree.tradecatlabs.com/`

## Reproduction

删除资源路径归一化行后执行原 smoke：

```bash
bash <(grep -v 'tech_tree_chunk="/' wiki/scripts/smoke-pages-release.sh)
```

结果稳定失败，并请求不存在的主机
`tree.tradecatlabs.com_next`。

## Observations

- O1：科技树首页和独立 chunk 请求均可直接返回 HTTP 200。
- O2：首页使用相对路径 `_next/static/...`，没有前导 `/`。
- O3：旧 smoke 使用 `"$tech_tree_url$tech_tree_chunk"` 直接拼接。
- O4：错误主机名恰好等于域名与相对路径首段的串联结果。

## Hypotheses

### H1：Cloudflare 自定义域名绑定错误

- Supports：失败发生在自定义域名请求阶段。
- Conflicts：直接请求首页返回 HTTP 200。
- Test：独立请求首页和 DNS。
- Verdict：rejected

### H2：本地代理间歇性改写目标主机

- Supports：环境存在 HTTP 代理。
- Conflicts：命令追踪显示调用前 URL 已经是错误主机名。
- Test：使用 `bash -x` 观察传给 `curl` 的完整参数。
- Verdict：rejected

### H3：相对 chunk 路径缺少根路径归一化（ROOT HYPOTHESIS）

- Supports：`tech_tree_chunk` 为 `_next/...`，拼接后恰好生成错误主机。
- Conflicts：无。
- Test：在拼接前统一补一个前导 `/`。
- Verdict：confirmed

## Experiments

### E1：规范化相对 chunk 路径

- Hypothesis：H3
- Change：执行 `tech_tree_chunk="/${tech_tree_chunk#/}"`。
- Expected：相对路径和根路径都规范化为单个前导 `/`。
- Result：原 smoke 完整通过；删除该行后再次以相同错误失败。
- Verdict：confirmed
- Revert：删除该归一化行即可回放旧故障。

## Root Cause

验证脚本假定科技树 chunk 地址自带前导 `/`，但 Next.js 产物返回相对路径
`_next/...`；域名与相对路径直接串联后生成了不存在的主机名。

## Fix

在请求 chunk 前执行一次幂等的根路径归一化，不修改科技树、Cloudflare
配置、网络代理或发布架构。

## Regression Evidence

- RED：`runtime/regression/pages-smoke-relative-chunk-red.json`
- GREEN：`runtime/regression/pages-smoke-relative-chunk-green.json`
- 反事实：`runtime/regression/pages-smoke-relative-chunk-counterfactual.json`
- 契约：`REGRESSION_EVIDENCE-pages-smoke-relative-chunk.json`

## Audit Case Sampling

不新增独立 audit case：该缺陷的复发信号就是 smoke 产生包含
`_next` 的错误主机名，现有脚本中的路径归一化与完整生产 smoke 已直接成为
owning gate。
