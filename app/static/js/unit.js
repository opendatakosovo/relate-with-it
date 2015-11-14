(function() {
	[].slice.call( document.querySelectorAll( '.unit-item' ) ).forEach( function( el ) {
		var stack_grid = $('.stack-grid');
		var images = [1,2,3,4];
		el.addEventListener( 'click', function() {
				if( classie.hasClass( stack_grid[0], 'active' ) ) {
					classie.removeClass( stack_grid[0], 'active' );
					var clicked_image_id = this.id;

					if(clicked_image_id == 1){
						$(".item1").css('transform', 'scale(1)');
						$(".item2").css('transform', 'scale(0)');
						$(".item3").css('transform', 'scale(0)');
						$(".item4").css('transform', 'scale(0)');
						$(".unit-item img:nth-child(1)").css('transform-origin','100% 100%');
						$(".unit-item img:nth-child(2)").css('transform-origin','0 100%');
						$(".unit-item img:nth-child(3)").css('transform-origin','100% 0%');
						$(".unit-item img:nth-child(4)").css('transform-origin','0 0');

					}else if(clicked_image_id == 2){

						$(".item1").css('transform', 'scale(0)');
						$(".item2").css('transform', 'scale(1)');
						$(".item3").css('transform', 'scale(0)');
						$(".item4").css('transform', 'scale(0)');
						$(".unit-item img:nth-child(1)").css('transform-origin','100% 100%');
						$(".unit-item img:nth-child(2)").css('transform-origin','0 100%');
						$(".unit-item img:nth-child(3)").css('transform-origin','100% 0%');
						$(".unit-item img:nth-child(4)").css('transform-origin','0 0');
					}
					else if(clicked_image_id == 3){
						$(".item1").css('transform', 'scale(0)');
						$(".item2").css('transform', 'scale(0)');
						$(".item3").css('transform', 'scale(1)');
						$(".item4").css('transform', 'scale(0)');
						$(".unit-item img:nth-child(1)").css('transform-origin','100% 100%');
						$(".unit-item img:nth-child(2)").css('transform-origin','0 100%');
						$(".unit-item img:nth-child(3)").css('transform-origin','100% 0%');
						$(".unit-item img:nth-child(4)").css('transform-origin','0 0');
					}
					else if(clicked_image_id == 4){
						$(".item1").css('transform', 'scale(0)');
						$(".item2").css('transform', 'scale(0)');
						$(".item3").css('transform', 'scale(0)');
						$(".item4").css('transform', 'scale(1)');
						$(".unit-item img:nth-child(1)").css('transform-origin','100% 100%');
						$(".unit-item img:nth-child(2)").css('transform-origin','0 100%');
						$(".unit-item img:nth-child(3)").css('transform-origin','100% 0%');
						$(".unit-item img:nth-child(4)").css('transform-origin','0 0');
					}

				}
				else {
					classie.addClass( stack_grid[0], 'active' );
					$(".item1").css('transform', 'scale(0.48)');
					$(".item2").css('transform', 'scale(0.480)');
					$(".item3").css('transform', 'scale(0.480)');
					$(".item4").css('transform', 'scale(0.481)');
				}
			} );
	} );
})();
