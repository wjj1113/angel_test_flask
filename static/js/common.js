
// 블럭 div 팝업 닫기버튼으로 클릭시 닫기
$(document).ready(function() { 
	$('#div_popup_close').click(function() {
		$('#div_popup_box').css("display", "none");
	});
	$('#div_popup_box').click(function() {
		//$('#div_popup_box').css("display", "none");
	});
});

// 블럭 div 팝업 닫기
function div_block_popup_close(){
	$('#div_popup_box').css("display", "none");
}

// 블럭 div 팝업 열기
function div_block_popup(width, height, src, opt){

	$('#div_popup_box').css("display", "block");
	
	$('#div_popup').css({ 
		top:  ($(window).height() - height) /2 + 'px', 
		left: ($(window).width() - width) /2 + 'px', 
		width: width+'px',
		height: height+'px'
	});

	if(opt){
		if (web_browser_check()=="IE" || web_browser_check()=="IE11" ){
			var innerHtmlStr	= "<iframe name='div_popup_ifm' id='div_popup_ifm' src='"+url+"' frameborder='0' scrolling='yes' style='width:100%;height:100%;'></iframe>";
			$('#div_popup').html(innerHtmlStr);
		}else{
			$('#div_popup_ifm').attr("scrolling", "yes");
		}
	}else{
		$('#div_popup_ifm').attr("scrolling", "no");
	}

}

// 블럭 div 팝업 열기
function div_block_popup2(width, height, src, opt){

	$('#div_popup_box').css("display", "block");
	
	$('#div_popup').css({ 
		top:  ($(window).height() - height) /2 + 'px', 
		left: ($(window).width() - width) /2 + 'px', 
		width: width+'px',
		height: height+'px'
	});

	if(opt){
		if (web_browser_check()=="IE" || web_browser_check()=="IE11" ){
			var innerHtmlStr	= "<iframe name='div_popup_ifm' id='div_popup_ifm' src='"+src+"' frameborder='0' scrolling='yes' style='width:100%;height:100%;'></iframe>";
			$('#div_popup').html(innerHtmlStr);
		}else{
			$('#div_popup_ifm').attr("scrolling", "yes");
			$('#div_popup_ifm').attr("src", src);
		}
	}else{
		$('#div_popup_ifm').attr("scrolling", "no");
		$('#div_popup_ifm').attr("src", src);
	}
}

function getCookie( name ){
	var nameOfCookie = name + "=";
	var x = 0;
	while ( x <= document.cookie.length ){
		var y = (x+nameOfCookie.length);
		if ( document.cookie.substring( x, y ) == nameOfCookie ) {
			if ( (endOfCookie=document.cookie.indexOf( ";", y )) == -1 )
			endOfCookie = document.cookie.length;
			return unescape( document.cookie.substring( y, endOfCookie ) );
		}
		x = document.cookie.indexOf( " ", x ) + 1;
		if ( x == 0 )
		break;
	}
	return "";
}

function setCookie( name, value, expiresday )  {
	var todayDate  = new Date();
	todayDate.setDate( todayDate.getDate() + expiresday );
	document.cookie = name + "=" + escape( value ) + "; path=/; expires=" + todayDate.toGMTString() + ";"
}

// 웹브라우저 체크
function web_browser_check(){
	var agt = navigator.userAgent.toLowerCase();
	if (agt.indexOf("chrome") != -1) return 'Chrome'; 
	if (agt.indexOf("opera") != -1) return 'Opera'; 
	if (agt.indexOf("staroffice") != -1) return 'Star Office'; 
	if (agt.indexOf("webtv") != -1) return 'WebTV'; 
	if (agt.indexOf("beonex") != -1) return 'Beonex'; 
	if (agt.indexOf("chimera") != -1) return 'Chimera'; 
	if (agt.indexOf("netpositive") != -1) return 'NetPositive'; 
	if (agt.indexOf("phoenix") != -1) return 'Phoenix'; 
	if (agt.indexOf("firefox") != -1) return 'Firefox'; 
	if (agt.indexOf("safari") != -1) return 'Safari'; 
	if (agt.indexOf("skipstone") != -1) return 'SkipStone'; 
	if (agt.indexOf("trident/4.0") != -1) return 'IE8'; 
	if (agt.indexOf("trident/5.0") != -1) return 'IE9'; 
	if (agt.indexOf("trident/6.0") != -1) return 'IE10'; 
	if (agt.indexOf("msie") != -1) return 'IE'; 
	if (agt.indexOf("trident/7.0") != -1) return 'IE11'; 
	if (agt.indexOf("netscape") != -1) return 'Netscape'; 
	if (agt.indexOf("mozilla/5.0") != -1) return 'Mozilla'; 
}

/**
 * 우편번호 창
 **/
var win_zipcode = function(frm_name, frm_zip1, frm_zip2, frm_addr1, frm_addr2, frm_addr3) {
    if(typeof daum === 'undefined'){
        alert("다음 juso.js 파일이 로드되지 않았습니다.");
        return false;
    }

    new daum.Postcode({
        oncomplete: function(data) {
            // 팝업에서 검색결과 항목을 클릭했을때 실행할 코드를 작성하는 부분.
            // 우편번호와 주소 정보를 해당 필드에 넣고, 커서를 상세주소 필드로 이동한다.
            var of = document[frm_name];
            of[frm_zip1].value = data.postcode1;
            of[frm_zip2].value = data.postcode2;
            of[frm_addr1].value = data.address1;
            of[frm_addr2].value = "";
            of[frm_addr3].value = "";

            if( data.addressType == "R" ){  //도로명이면
                of[frm_addr3].value = data.address2;
            }

            of[frm_addr2].focus();
        }
    }).open();
}



// *************************************************************
// 숫자 체크
// *************************************************************
function checkMoneyUpdate(el){
	key = event.keyCode;
	if(event.keyCode == 8 || event.keyCode == 46 || event.keyCode == 109 || event.keyCode == 110 || event.keyCode == 189 || event.keyCode == 190 || (event.keyCode >= 48 && event.keyCode <= 57) || (event.keyCode >= 96 && event.keyCode <= 105))
		return el.value = addComma_new(el.value);
	else
		//alert("숫자 형태로 입력하세요!");
		//el.value = el.value;
		return;
}

// ---------------------------------------------------------
// 콤마 처리가 가능한 금액포멧 스크립트 (문자열은 필터링 되지 않음)
// ---------------------------------------------------------
function addComma_new(txt){
	var min,tmp,str,v;
	txt = removeComma(txt);
	min = txt.substring(0,1) == "-" ? txt.substring(0,1) : "";
	txt = txt.replace(min,'');
	tmp = txt.split('.');
	str = new Array();
	v = tmp[0].replace(/,/gi,'');
	for(var i=0;i<=v.length;i++){
		str[str.length] = v.charAt(v.length-i);
		if(i%3==0 && i!=0 && i!=v.length){
			str[str.length]='.';
		}
	}
	str = min+str.reverse().join('').replace(/\./gi,',');
	return(tmp.length == 2) ? str+'.'+tmp[1] : str;
}

function isNumber(evt) {
    evt = (evt) ? evt : window.event;
    var charCode = (evt.which) ? evt.which : evt.keyCode;
    if (charCode > 31 && (charCode < 48 || charCode > 57)) {
        return false;
    }
    return true;
}

// ---------------------------------------------------------
// 콤마 제거
// ---------------------------------------------------------
function removeComma(str) {
	str = str + "";
	str = $.trim(str);
	var len = str.length;
	var retval = "";
	for(var i = 0; i < len ; i++) {
		if (str.charAt(i) != ",") {
			retval += str.charAt(i);
		}
	}
	return retval;
}



// 쿠키 입력
function set_cookie(name, value, expirehours, domain){
    var today = new Date();
    today.setTime(today.getTime() + (60*60*1000*expirehours));
    document.cookie = name + "=" + escape( value ) + "; path=/; expires=" + today.toGMTString() + ";";
    if (domain) {
        document.cookie += "domain=" + domain + ";";
    }
}

// 쿠키 얻음
function get_cookie(name){
    var find_sw = false;
    var start, end;
    var i = 0;

    for (i=0; i<= document.cookie.length; i++){
        start	= i;
        end		= start + name.length;

        if(document.cookie.substring(start, end) == name){
            find_sw = true
            break
        }
    }

    if (find_sw == true){
        start = end + 1;
        end = document.cookie.indexOf(";", start);

        if(end < start)
            end = document.cookie.length;

        return unescape(document.cookie.substring(start, end));
    }
    return "";
}

// 쿠키 지움
function delete_cookie(name){
    var today = new Date();

    today.setTime(today.getTime() - 1);
    var value = get_cookie(name);
    if(value != "")
        document.cookie = name + "=" + value + "; path=/; expires=" + today.toGMTString();
}
