django.jQuery.urlParam = function(name, defaultValue, url) {
	if (!url) {
		url = window.location.href
	}
	var results = new RegExp('[\\?&]'+name+'=([^&#]*)').exec(url);
	return results ? results[1] : defaultValue;
}

django.jQuery.scriptUrlParam = function(js, name, defaultValue) {
	result = defaultValue;
	django.jQuery('head script[src]').each(function() {
		if (this.src.match(js)) {
			result = django.jQuery.urlParam(name, result, this.src);
		}
	});
	return result;
}
