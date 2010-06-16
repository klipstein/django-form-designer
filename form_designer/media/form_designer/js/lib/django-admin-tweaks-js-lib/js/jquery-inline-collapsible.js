function makeCollapsible(target, item, collapsible, triggerTarget, setInitStatus, setFirstStatus)
{
	var triggerExpand = gettext('Show');
	var triggerCollapse = gettext('Hide');
	var triggerLink = '<a href="javascript:void(0)"></a>';
	var triggerPrepend = ' ( ';
	var triggerAppend = ' )';
	
	django.jQuery(target).find(item).each(function(i) {
		django.jQuery(this).find(collapsible).slideUp(1);
		
		var trigger = django.jQuery(triggerLink)
		django.jQuery(this).find(triggerTarget).append(trigger);
		trigger.before(triggerPrepend);
		trigger.after(triggerAppend);
		var item = this
		var toggleCollapse = function(status, speed)
		{
			if (status == null) {
				status = !item.collapseStatus;
			}
			if (speed == null) {
			    speed = 1;
			}
			item.collapseStatus = status;
			if (status) {
				trigger.html(triggerCollapse);
				django.jQuery(item).find(collapsible).slideDown(speed);
			} else {
				trigger.html(triggerExpand);
				django.jQuery(item).find(collapsible).slideUp(speed);
			}
		}

		trigger.click(function(event) {
			event.preventDefault();
			toggleCollapse(null, 'normal')
		})

		// Collapse by default unless there are errors
		initStatus = setInitStatus != null ? setInitStatus : django.jQuery(this).find('.errors').length != 0;
		firstStatus = setFirstStatus != null ? setFirstStatus : initStatus;

		toggleCollapse(i == 0 ? firstStatus : initStatus)
	});
}

(function($) {
	$(document).ready(function() {
		makeCollapsible('div.inline-group', 'div.inline-related', 'fieldset', 'h3 b');
	});
})(django.jQuery);
