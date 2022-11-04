(function($){
	$(document).ready(function() {
		$(".smarteditor2").each( function(index){
			var get_id = $(this).attr("id");

			if( !get_id || $(this).prop("nodeName") != 'TEXTAREA' ) return true;

			nhn.husky.EZCreator.createInIFrame({
				oAppRef: oEditors,
				elPlaceHolder: get_id,
				sSkinURI: rPath + "/module/SmartEditor/SmartEditor2Skin.html",
				htParams : {
					bUseToolbar : true,			
					bUseVerticalResizer : true,	
					bUseModeChanger : true,			
					fOnBeforeUnload : function(){
						//
					}
				}, //boolean
				fOnAppLoad : function(){
					//
				},
				fCreator: "createSEditor2"
			});
		});
	});
})(jQuery);
