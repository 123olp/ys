<?php

// ==================== Human Infra 站点策略 ====================

$wgSitename = getenv( 'WIKI_SITE_NAME' ) ?: 'Human Infra Wiki';
$wgMetaNamespace = 'Human_Infra';
$wgLanguageCode = 'zh';
$wgLocaltimezone = 'Asia/Shanghai';
$wgDefaultSkin = 'vector-2022';
$wgMainPageIsDomainRoot = true;

// Portal 是受治理的专题导航层，不承载独立证据结论。
define( 'NS_HUMAN_INFRA_PORTAL', 100 );
define( 'NS_HUMAN_INFRA_PORTAL_TALK', 101 );
$wgExtraNamespaces[NS_HUMAN_INFRA_PORTAL] = 'Portal';
$wgExtraNamespaces[NS_HUMAN_INFRA_PORTAL_TALK] = 'Portal_talk';
$wgNamespaceAliases['门户'] = NS_HUMAN_INFRA_PORTAL;
$wgContentNamespaces[] = NS_HUMAN_INFRA_PORTAL;
$wgLogos = [
    'icon' => "$wgResourceBasePath/resources/assets/human-infra-mark.svg",
];

wfLoadSkin( 'Vector' );
wfLoadExtension( 'Cite' );
wfLoadExtension( 'ParserFunctions' );
wfLoadExtension( 'TemplateStyles' );
wfLoadExtension( 'VisualEditor' );
wfLoadExtension( 'PageForms' );

$wgEnableUploads = true;
$wgFileExtensions[] = 'pdf';
$wgFileExtensions[] = 'svg';
$wgUseInstantCommons = true;
$wgEnableEmail = false;
$wgEnableUserEmail = false;

// 公开阅读、受控编辑。管理员可在 Wiki 内创建后续账号和权限组。
$wgGroupPermissions['*']['read'] = true;
$wgGroupPermissions['*']['edit'] = false;
$wgGroupPermissions['*']['createpage'] = false;
$wgGroupPermissions['*']['createtalk'] = false;
$wgGroupPermissions['*']['createaccount'] = false;
$wgGroupPermissions['user']['createclass'] = false;
$wgGroupPermissions['user']['multipageedit'] = false;
$wgGroupPermissions['sysop']['createclass'] = true;
$wgGroupPermissions['sysop']['multipageedit'] = true;

$wgDefaultUserOptions['visualeditor-editor'] = 'visualeditor';
$wgDefaultUserOptions['vector-font-size'] = 1;
$wgVisualEditorEnableWikitext = true;

$wgRightsPage = 'Human_Infra:版权';
$wgRightsUrl = 'https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans';
$wgRightsText = 'CC BY-SA 4.0';
$wgRightsIcon = "$wgResourceBasePath/resources/assets/licenses/cc-by-sa.png";

$wgJobRunRate = 0;
$wgShowExceptionDetails = false;
$wgShowDBErrorBacktrace = false;

if ( getenv( 'WIKI_SERVER' ) ) {
    $wgServer = getenv( 'WIKI_SERVER' );
}
