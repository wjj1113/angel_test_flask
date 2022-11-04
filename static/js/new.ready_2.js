// 이미지 미리로딩 스크립트
function preload(arrayOfImages) {
    $(arrayOfImages).each(function(){
        $('<img/ >')[0].src = this;
    });
}

// 메일 구독 스크립트
function subscribe(){
    var email = $("#email").val();
    if(!email){
        alert("이메일 주소를 입력하세요.");
        return;
    }

    $.ajax({
        type: "POST",
        url: "https://api.buencamino.io/api/just/v1/notice/subscriber/email",
        dataType: "json",
        data: { "email": email },
        cache: false,
        async: false,
        success: function(data) {
            // result = data;
            // console.log(data.result);
            if(data.result=="SUCCESS"){
                alert("출시 소식 신청이 되었습니다.");
            }else{
                alert("Oops, 정상적으로 처리가 안되었습니다.");
            }
        },
    });
}

/* 이메일 입력창의 힌트 메세지 세팅 */
function setEmailInputPlaceholderText(){
    if( $(this).width() < 769 ) {
        $("#email").attr('placeholder', '이메일 입력하고 출시 소식 받기');
    } else {
        $("#email").attr('placeholder', 'JUST 출시 소식을 가장 먼저 받고 싶다면? 이메일 주소를 입력');
    }
}

// 로드 완료
$(document).ready(function(){
    /* SECTION03의 슬라이드 초기화 */
    var bxSlider = $('.bxslider').bxSlider({ // https://bxslider.com/options
        auto: true,
        pause: 3000, // default
        // pause: 1000, // test
        responsive: true,
        adaptiveHeight: false,
        controls: false,
        onSliderLoad: function(){
            $('.bx-controls a').on('click', function(){
                setTimeout(function() { 
                    bxSlider.stopAuto();
                }, 1000);
                setTimeout(function() {
                    bxSlider.startAuto();
                }, 2000);
            })
        },
        onSlideAfter: function($slideElement, oldIndex, newIndex){
            bxSlider.stopAuto();
            bxSlider.startAuto();
        }
    });

    /* SECTION04의 탭 이벤트 바인딩 */
    $('#SECTION04 .tab-title').on('click', function(){
        // 탭 타이틀 변경
        $('#SECTION04 .tab-title').removeClass('on');
        $(this).addClass('on');
        // 탭 컨텐츠 변경
        var targetId = $(this).data('for');
        $('#SECTION04 .tab-content').removeClass('on');
        $(targetId).addClass('on');
        // 이미지 변경
        var imgSrc = $(this).data('img');
        $("#TAB1_IMG").attr('src', imgSrc);
    });

    /* SECTION05의 탭 이벤트 바인딩 */
    $('#SECTION05 .tab-title-text').on('click', function(){
        // 탭 타이틀 변경
        $('#SECTION05 .tab-title-text').removeClass('on');
        $(this).addClass('on');

        // 탭 타이틀 텍스트 변경
        var targetId = $(this).data('for');
        $('#SECTION05 .title-text').removeClass('on');
        $(targetId+"2").addClass('on');


        // 탭 컨텐츠 타이틀 변경
        var targetId = $(this).data('for');
        $('#SECTION05 .tab-content-title').removeClass('on');
        $(targetId).addClass('on');

        // 탭 컨텐츠 변경
        var targetId = $(this).data('for');
        $('#SECTION05 .tab-content').removeClass('on');
        $(targetId).addClass('on');

        // 이미지 변경
        $('#SECTION05 .tab-title-text img').each(function(item){
            $(this).attr('src', $(this).data('src'));
        });

        var selectedNo = $(this).data('no');
        $(this).find("img").attr('src', '/images/main_pc/g5_tab_0'+ selectedNo +'_over.png')
        $("#TAB2_IMG").attr('src', '/images/main_pc/s3_0'+ selectedNo +'.png');

    });

    /* SECTION07의 슬라이드 초기화 */
    $('.flex-slider.only-desktop').flexslider({
        selector: ".slides > li",
        animation: "slide",
        animationLoop: true,
        move: 3,
        // slideshowSpeed: 1000, //test
        slideshowSpeed: 3000,
        controlNav: false,
        customDirectionNav: $(".slide-nav-wrap a"),
        drag: true,
        start: function(slider){
            if (slider.vars.drag) {
                // 마우스 드래그 이벤트 확장 (PC)
                slider.bind('udragstart.udrag', function(event) {
                    event.preventDefault();
                    var target = (event.px_delta_x < 0) ? slider.getTarget('next') : slider.getTarget('prev');
                    slider.flexAnimate(target, slider.vars.pauseOnAction);
                });
            }
        },
    });
    $('.flex-slider.only-mobile').flexslider({
        selector: ".slides > li",
        animation: "slide",
        animationLoop: true,
        move: 1,
        slideshowSpeed: 3000,
        controlNav: false,
        customDirectionNav: $(".slide-mobile-nav-wrap a"),
    });

    /* 이메일 입력창의 힌트 메세지 세팅 */
    setEmailInputPlaceholderText();

    // 슬라이더 다음 이미지 프리로딩
    preload([
        '/images/main_pc/g4_01.png',
        '/images/main_pc/g4_02.png',
        '/images/main_pc/g4_03.png'
    ]);
    preload([
        '/images/main_pc/g5_01.png',
        '/images/main_pc/g5_02.png',
        '/images/main_pc/g5_03.png',
        '/images/main_pc/g5_04.png',
        '/images/main_pc/g5_05.png',
        '/images/main_pc/g5_06.png'
    ]);
});

// 창 크기가 변경된 경우
$(window).on('resize', function(){
    /* 이메일 입력창의 힌트 메세지 세팅 */
    setEmailInputPlaceholderText();
    // 기타 반응형 대응 필요한 요소 제어
    if( $(this).width() < 769 ) {
        $("#group_06_img").attr('src', '/images/main_mobile/g6.png');
        $("#subscribe-button").attr('src', '/images/main_mobile/g9_btn.png');
    } else {
        $("#group_06_img").attr('src', '/images/main_pc/g6.png');
        $("#subscribe-button").attr('src', '/images/main_pc/g9_btn.png');
    }
});
