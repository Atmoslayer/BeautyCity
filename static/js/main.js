$(document).ready(function() {
	$('.salonsSlider').slick({
		arrows: true,
	  slidesToShow: 4,
	  infinite: true,
	  prevArrow: $('.salons .leftArrow'),
	  nextArrow: $('.salons .rightArrow'),
	  responsive: [
	    {
	      breakpoint: 991,
	      settings: {
	        
	      	centerMode: true,
  			//centerPadding: '60px',
	        slidesToShow: 2
	      }
	    },
	    {
	      breakpoint: 575,
	      settings: {
	        slidesToShow: 1
	      }
	    }
	  ]
	});
	$('.servicesSlider').slick({
		arrows: true,
	  slidesToShow: 4,
	  prevArrow: $('.services .leftArrow'),
	  nextArrow: $('.services .rightArrow'),
	  responsive: [
	  	{
	      breakpoint: 1199,
	      settings: {
	        

	        slidesToShow: 3
	      }
	    },
	    {
	      breakpoint: 991,
	      settings: {
	        
	      	centerMode: true,
  			//centerPadding: '60px',
	        slidesToShow: 2
	      }
	    },
	    {
	      breakpoint: 575,
	      settings: {
	        slidesToShow: 1
	      }
	    }
	  ]
	});

	$('.mastersSlider').slick({
		arrows: true,
	  slidesToShow: 4,
	  prevArrow: $('.masters .leftArrow'),
	  nextArrow: $('.masters .rightArrow'),
	  responsive: [
	  	{
	      breakpoint: 1199,
	      settings: {
	        

	        slidesToShow: 3
	      }
	    },
	    {
	      breakpoint: 991,
	      settings: {
	        

	        slidesToShow: 2
	      }
	    },
	    {
	      breakpoint: 575,
	      settings: {
	        slidesToShow: 1
	      }
	    }
	  ]
	});

	$('.reviewsSlider').slick({
		arrows: true,
	  slidesToShow: 4,
	  prevArrow: $('.reviews .leftArrow'),
	  nextArrow: $('.reviews .rightArrow'),
	  responsive: [
	  	{
	      breakpoint: 1199,
	      settings: {
	        

	        slidesToShow: 3
	      }
	    },
	    {
	      breakpoint: 991,
	      settings: {
	        

	        slidesToShow: 2
	      }
	    },
	    {
	      breakpoint: 575,
	      settings: {
	        slidesToShow: 1
	      }
	    }
	  ]
	});

	// menu
	$('.header__mobMenu').click(function() {
		$('#mobMenu').show()
	})
	$('.mobMenuClose').click(function() {
		$('#mobMenu').hide()
	})

	new AirDatepicker('#datepickerHere', {
		onSelect({date, formattedDate, datepicker}) {
			sessionStorage.setItem("appointment_date", formattedDate);
		}
	}) 

	var acc = document.getElementsByClassName("accordion");
	var i;

	for (i = 0; i < acc.length; i++) {
	  acc[i].addEventListener("click", function(e) {
	  	e.preventDefault()
	    this.classList.toggle("active");
	    var panel = $(this).next()
	    panel.hasClass('active') ?  
	    	 panel.removeClass('active')
	    	: 
	    	 panel.addClass('active')
	  });
	}

	$(document).on('click', '.accordion__block', function(e) {
		let thisName,thisAddress;

		thisName = $(this).find('> .accordion__block_intro').text()
		thisAddress = $(this).find('> .accordion__block_address').text()
		
		$.ajax({
			type: "get",
			url: "/api/masters/",
			data: {
				salon: thisAddress
			},
			success: function(response) {
				let parse_response = JSON.parse(response)
				let master_block = ""
				for (let key in parse_response) {
					master_block = master_block + '<div class="accordion__block_item fic"><div class="accordion__block_item_intro">' + parse_response[key]['fields']['first_name'] +' '+ parse_response[key]['fields']['last_name']+ '</div></div>'
				}
				master_block = '<div class="accordion__block_items">' + master_block + '</div>'
				$('.service__masters > .panel').html(master_block)
			}
		});
		if(thisName === 'BeautyCity ????????????????????') {
			$('.service__masters > .panel').html(`
				<div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/all.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">?????????? ????????????</div>
						  	</div>
						  </div>
						  <div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/pushkinskaya/1.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">?????????????????? ????????????</div>
						  	</div>
						  	<div class="accordion__block_prof">???????????? ????????????????</div>
						  </div>
						  <div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/pushkinskaya/2.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">???????? ????????????????</div>
						  	</div>
						  	<div class="accordion__block_prof">????????????????????</div>
						  </div>
						  <div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/pushkinskaya/3.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">?????? ????????????????</div>
						  	</div>
						  	<div class="accordion__block_prof">????????????????</div>
						  </div>
						  <div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/pushkinskaya/4.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">?????????? ????????????????</div>
						  	</div>
						  	<div class="accordion__block_prof">??????????????</div>
						  </div>
						  <div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/pushkinskaya/5.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">?????????? ??????????????????</div>
						  	</div>
						  	<div class="accordion__block_prof">????????????????</div>
						  </div>
						  <div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/pushkinskaya/6.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">?????????????????? ????????????????</div>
						  	</div>
						  	<div class="accordion__block_prof">????????????????</div>
						  </div>	
			`)
			// $('.service__masters div[data-masters="Pushkinskaya"]').addClass('vib')
		}
		if(thisName === 'BeautyCity ????????????') {
			
			$('.service__masters > .panel').html(`
				<div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/all.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">?????????? ????????????</div>
						  	</div>
						  </div>
						  <div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/lenina/1.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">?????????? ??????????????????</div>
						  	</div>
						  	<div class="accordion__block_prof">???????????? ????????????????</div>
						  </div>
						  <div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/lenina/2.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">?????????? ????????????????</div>
						  	</div>
						  	<div class="accordion__block_prof">????????????????????</div>
						  </div>
						  <div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/lenina/3.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">???????????? ????????????????</div>
						  	</div>
						  	<div class="accordion__block_prof">????????????????</div>
						  </div>
						  <div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/lenina/4.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">?????????? ??????????????</div>
						  	</div>
						  	<div class="accordion__block_prof">??????????????</div>
						  </div>
						  <div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/lenina/5.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">???????????? ??????????????????</div>
						  	</div>
						  	<div class="accordion__block_prof">????????????????</div>
						  </div>
						  <div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/lenina/6.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">???????? ??????????????????</div>
						  	</div>
						  	<div class="accordion__block_prof">????????????????</div>
						  </div>
			`)
		}

		if(thisName === 'BeautyCity ??????????????') {
			$('.service__masters > .panel').html(`
				<div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/all.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">?????????? ????????????</div>
						  	</div>
						  </div>
						  <div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/krasnaya/1.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">?????? ????????????????</div>
						  	</div>
						  </div>
						  <div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/krasnaya/2.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">?????????? ????????????</div>
						  	</div>
						  	<div class="accordion__block_prof">???????????? ????????????????</div>
						  </div>
						  <div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/krasnaya/3.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">?????????? ????????????</div>
						  	</div>
						  	<div class="accordion__block_prof">????????????????????</div>
						  </div>
						  <div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/krasnaya/4.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">?????? ????????????????</div>
						  	</div>
						  	<div class="accordion__block_prof">????????????????</div>
						  </div>
						  <div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/krasnaya/5.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">???????? ????????????????</div>
						  	</div>
						  	<div class="accordion__block_prof">??????????????</div>
						  </div>
						  <div class="accordion__block fic">
						  	<div class="accordion__block_elems fic">
							  	<img src="img/masters/avatar/krasnaya/6.svg" alt="avatar" class="accordion__block_img">
							  	<div class="accordion__block_master">?????????????? ??????????</div>
						  	</div>
						  	<div class="accordion__block_prof">????????????????</div>
						  </div>
			`)

		}
		sessionStorage.setItem('salon', thisAddress)
		$(this).parent().parent().find('> button.active').addClass('selected').text(thisName + '  ' +thisAddress)
		setTimeout(() => {
			$(this).parent().parent().find('> button.active').click()
		}, 200)
		
		// $(this).parent().addClass('hide')

		// console.log($(this).parent().parent().find('.panel').hasClass('selected'))
		
		// $(this).parent().parent().find('.panel').addClass('selected')
	})


	$(document).on('click', '.service__services .accordion__block_item', function(e) {
		thisService = $(this).find('> .accordion__block_item_intro').text()
		thisPrice = $(this).find('> .accordion__block_item_address').text()
		sessionStorage.setItem('service_name', thisService)
		sessionStorage.setItem('service_price', thisPrice)
		$(this).parent().parent().parent().parent().find('> button.active').addClass('selected').text(thisService+ '  ' +thisPrice)
		// $(this).parent().parent().parent().parent().find('> button.active').click()
		// $(this).parent().parent().parent().addClass('hide')
		setTimeout(() => {
			$(this).parent().parent().parent().parent().find('> button.active').click()
		}, 200)
	})



	// 	console.log($('.service__masters > .panel').attr('data-masters'))
	// if($('.service__salons .accordion.selected').text() === "BeautyCity ????????????????????  ????. ????????????????????, ??. 78??") {
	// }e


	$(document).on('click', '.service__masters .accordion__block_item', function(e) {
		//let clone = $(this).clone()
		// console.log(clone)
		thisEmployer = $(this).find('> .accordion__block_item_intro').text()
		sessionStorage.setItem('serviceman', thisEmployer)
		$(this).parent().parent().parent().find('> button.active').addClass('selected').text(thisEmployer)
		// $(this).parent().parent().find('> button.active').html(clone)
		setTimeout(() => {
			$(this).parent().parent().parent().find('> button.active').click()
		}, 200)
	})

	// $('.accordion__block_item').click(function(e) {
	// 	const thisName = $(this).find('.accordion__block_item_intro').text()
	// 	const thisAddress = $(this).find('.accordion__block_item_address').text()
	// 	console.log($(this).parent().parent().parent().parent())
	// 	$(this).parent().parent().parent().parent().find('button.active').addClass('selected').text(thisName + '  ' +thisAddress)
	// })



	// $('.accordion__block_item').click(function(e) {
	// 	const thisChildName = $(this).text()
	// 	console.log(thisChildName)
	// 	console.log($(this).parent().parent().parent())
	// 	$(this).parent().parent().parent().parent().parent().find('button.active').addClass('selected').text(thisChildName)

	// })
	// $('.accordion.selected').click(function() {
	// 	$(this).parent().find('.panel').hasClass('selected') ? 
	// 	 $(this).parent().find('.panel').removeClass('selected')
	// 		:
	// 	$(this).parent().find('.panel').addClass('selected')
	// })


	//popup
	$('.header__block_auth').click(function(e) {
		e.preventDefault()
		if ($(this).find('> .header__block_auth__intro').text() == '??????????') 
			window.location.href = '/authorization/';
		else
			window.location.href = '/account/';
	
	//$('.authPopup').arcticmodal();
	// $('#confirmModal').arcticmodal();

})

	$('.rewiewPopupOpen').click(function(e) {
		e.preventDefault()
		$('#reviewModal').arcticmodal();
	})
	$('.payPopupOpen').click(function(e) {
		e.preventDefault()
		$('#paymentModal').arcticmodal();
	})
	$('.tipsPopupOpen').click(function(e) {
		e.preventDefault()
		$('#tipsModal').arcticmodal();
	})
	
	$('.authPopup__form').submit(function() {
		$('#confirmModal').arcticmodal();
		return false
	})

	//service
	$('.time__items .time__elems_elem .time__elems_btn').click(function(e) {
		e.preventDefault()
		$('.time__elems_btn').removeClass('active')
		$(this).addClass('active')
		sessionStorage.setItem("appointment_time", $(this).text())
		// $(this).hasClass('active') ? $(this).removeClass('active') : $(this).addClass('active')
	})

	$(document).on('click', '.servicePage', function() {
		if($('.time__items .time__elems_elem .time__elems_btn').hasClass('active') && $('.service__form_block > button').hasClass('selected')) {
			$('.time__btns_next').addClass('active')
		}
	})
})
$(document).on('click', '.time__btns_next', function(e) {
	let csrf = document.cookie.replace(/(?:(?:^|.*;\s*)csrftoken\s*\=\s*([^;]*).*$)|^.*$/, "$1");
	$.ajax({
		type: "post",
		url: "/api/appointment/",
		data: {
			salon: sessionStorage.getItem('salon'),
			serviceman: sessionStorage.getItem('serviceman'),
			service_name: sessionStorage.getItem('service_name'),
			service_price:  sessionStorage.getItem('service_price'),
			appointment_date: sessionStorage.getItem('appointment_date'), 
			appointment_time: sessionStorage.getItem('appointment_time'),
			csrfmiddlewaretoken: csrf,
		},
		
		success: function(response) {
		    alert(response);
			console.log(response);
		}
	});
})
$(document).on('click', '#profile_change', function(e) {
	e.preventDefault()
    $('#profileModal').arcticmodal();
});