(function() {
	[].slice.call( document.querySelectorAll( '.stack-project' ) ).forEach( function( el ) {
		var togglebtt = el.previousElementSibling,
			togglefn = function() {
				if( classie.hasClass( el, 'active' ) ) {
					classie.removeClass( el, 'active' );
				}
				else {
					classie.addClass( el, 'active' );
				}
			};

		togglebtt.addEventListener( 'click', togglefn );
	} );
})();