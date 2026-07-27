/* Wikimedia portal DOM adapter. Visual behavior remains owned by upstream CSS. */
( function () {
	'use strict';

	const config = window.HUMAN_INFRA_PORTAL || { wikiPort: '18782' };
	const host = window.location.hostname || 'localhost';
	const port = config.wikiPort ? ':' + config.wikiPort : '';
	const wikiBase = config.wikiBase || window.location.protocol + '//' + host + port;

	function wikiUrl( title, language ) {
		const path = title === 'Human Infra:首页'
			? '/'
			: '/wiki/' + title.replaceAll( ' ', '_' ).split( '/' )
				.map( encodeURIComponent ).join( '/' ) + '/';
		const url = new URL( path, wikiBase );
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
		const searchInput = document.getElementById( 'searchInput' );
		const localSearchInput = searchInput && searchInput.cloneNode( true );
		const searchUrl = new URL( '/search/', wikiBase );

		searchForm.action = searchUrl.toString();
		searchForm.method = 'get';
		if ( localSearchInput ) {
			localSearchInput.name = 'q';
			searchInput.replaceWith( localSearchInput );
		}
		searchForm.addEventListener( 'submit', ( event ) => {
			event.preventDefault();
			const query = localSearchInput ? localSearchInput.value.trim() : '';
			const language = document.getElementById( 'searchLanguage' ).value;
			if ( query ) {
				const url = new URL( searchUrl );
				url.searchParams.set( 'q', query );
				url.searchParams.set( 'uselang', language );
				window.location.assign( url.toString() );
			}
		} );
	}

	document.body.classList.add( 'jsl10n-visible' );
}() );
