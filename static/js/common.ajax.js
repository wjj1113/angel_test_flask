var subscribe_send = function(email) {
    var result = "";
    $.ajax({
        type: "POST",
        url: "https://api.buencamino.io/api/just/v1/notice/subscriber/email",
		dataType: "json",
        data: {
            "email": email
        },
        cache: false,
        async: false,
        success: function(data) {
            result = data;
			console.log(data.result);
			if(data.result=="SUCCESS"){
				alert("정보 구독 신청이 되었습니다.");
			}else{
				alert("정상적으로 처리가 안되었습니다.");
			}
        }
    });
    return result;
}

