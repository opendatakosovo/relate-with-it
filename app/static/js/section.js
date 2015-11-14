(function() {
	[].slice.call( document.querySelectorAll( '.project-item' ) ).forEach( function( el ) {
		var stack_grid = $('.stack-project');
		el.addEventListener( 'click', function() {
				if( classie.hasClass( stack_grid[0], 'active' ) ) {
					classie.removeClass( stack_grid[0], 'active' );
					var clicked_image_id = this.id;

					if(clicked_image_id == 1){
						$(".pitem1").css('transform', 'scale(1)');
						$(".pitem2").css('transform', 'scale(0)');
						$(".pitem3").css('transform', 'scale(0)');
						$(".pitem4").css('transform', 'scale(0)');
						$(".unit-item img:nth-child(1)").css('transform-origin','100% 100%');
						$(".unit-item img:nth-child(2)").css('transform-origin','0 100%');
						$(".unit-item img:nth-child(3)").css('transform-origin','100% 0%');
						$(".unit-item img:nth-child(4)").css('transform-origin','0 0');

					}else if(clicked_image_id == 2){

						$(".pitem1").css('transform', 'scale(0)');
						$(".pitem2").css('transform', 'scale(1)');
						$(".pitem3").css('transform', 'scale(0)');
						$(".pitem4").css('transform', 'scale(0)');
						$(".unit-item img:nth-child(1)").css('transform-origin','100% 100%');
						$(".unit-item img:nth-child(2)").css('transform-origin','0 100%');
						$(".unit-item img:nth-child(3)").css('transform-origin','100% 0%');
						$(".unit-item img:nth-child(4)").css('transform-origin','0 0');
					}
					else if(clicked_image_id == 3){
						$(".pitem1").css('transform', 'scale(0)');
						$(".pitem2").css('transform', 'scale(0)');
						$(".pitem3").css('transform', 'scale(1)');
						$(".pitem4").css('transform', 'scale(0)');
						$(".unit-item img:nth-child(1)").css('transform-origin','100% 100%');
						$(".unit-item img:nth-child(2)").css('transform-origin','0 100%');
						$(".unit-item img:nth-child(3)").css('transform-origin','100% 0%');
						$(".unit-item img:nth-child(4)").css('transform-origin','0 0');
					}
					else if(clicked_image_id == 4){
						$(".pitem1").css('transform', 'scale(0)');
						$(".pitem2").css('transform', 'scale(0)');
						$(".pitem3").css('transform', 'scale(0)');
						$(".pitem4").css('transform', 'scale(1)');
						$(".unit-item img:nth-child(1)").css('transform-origin','100% 100%');
						$(".unit-item img:nth-child(2)").css('transform-origin','0 100%');
						$(".unit-item img:nth-child(3)").css('transform-origin','100% 0%');
						$(".unit-item img:nth-child(4)").css('transform-origin','0 0');
					}

				}
				else {
					classie.addClass( stack_grid[0], 'active' );
					var clicked_image_id = this.id;
					$(".pitem1").css('transform', 'scale(0.48)');
					$(".pitem2").css('transform', 'scale(0.480)');
					$(".pitem3").css('transform', 'scale(0.480)');
					$(".pitem4").css('transform', 'scale(0.481)');
				}
			} );
	} );
})();
