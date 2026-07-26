/* Wikimedia portal DOM adapter. Visual behavior remains owned by upstream CSS. */
( function () {
	'use strict';

	const config = window.HUMAN_INFRA_PORTAL || { wikiPort: '18782' };
	const host = window.location.hostname || 'localhost';
	const port = config.wikiPort ? ':' + config.wikiPort : '';
	const wikiBase = config.wikiBase || window.location.protocol + '//' + host + port;

	function wikiUrl( title, language ) {
		const url = new URL( wikiBase + '/index.php' );
		url.searchParams.set( 'title', title );
		if ( language ) {
			url.searchParams.set( 'uselang', language );
		}
		return url.toString();
	}

	document.querySelectorAll( '[data-hi-language]' ).forEach( ( link ) => {
		link.href = wikiUrl( 'Human Infra:首页', link.dataset.hiLanguage );
	} );

	document.querySelectorAll( '[data-hi-title]' ).forEach( ( link ) => {
		link.href = wikiUrl( link.dataset.hiTitle, 'zh' );
	} );

	document.querySelectorAll( '.langlist a[lang]' ).forEach( ( link ) => {
		link.href = wikiUrl( 'Human Infra:首页', link.getAttribute( 'lang' ) );
	} );

	const searchForm = document.getElementById( 'search-form' );
	if ( searchForm ) {
		searchForm.addEventListener( 'submit', ( event ) => {
			event.preventDefault();
			const query = document.getElementById( 'searchInput' ).value.trim();
			const language = document.getElementById( 'searchLanguage' ).value;
			if ( query ) {
				window.location.assign( wikiUrl( 'Special:Search', language ) + '&search=' + encodeURIComponent( query ) );
			}
		} );
	}

	document.body.classList.add( 'jsl10n-visible' );
}() );
