var PAAS_API = {

	open_other_app: function(app_code, app_url, refresh_tips){
		try{
            Bk_api.open_other_app(app_code, app_url, refresh_tips);
		}catch(err){
			console.error(err)
			if(err.name !== 'TypeError' && app_code === 'bk_cc'){
				window.location.href = BK_CC_HOST;
			}
		}
	},
}
