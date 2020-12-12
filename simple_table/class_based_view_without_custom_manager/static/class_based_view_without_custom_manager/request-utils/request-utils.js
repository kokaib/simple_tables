class RequestUtils {

	/**/
	
	static makeXHR(method, url, headers, body) {
		var xhr = new XMLHttpRequest();
		method = method.toLowerCase();
		if (method == 'get') {
			if (body != null) {
				if (!url.includes('?')) url += '?';
				for (var [name, value] of body.entries()) {
					if (!url.endsWith('?')) url += '&';
					url += name + '=' + value;
				}
			}
			xhr.open(method, url);
			RequestUtils.setXHRHeaders(xhr, headers)
			return xhr;
		} else if (method == 'post') {
			xhr.open(method, url);
			RequestUtils.setXHRHeaders(xhr, headers)
			return xhr;
		}
	}

	static setXHRHeaders(xhr, headers) {
		for ([header, value] of headers.entries()) {
			xhr.setRequestHeader(header, value);
		}
	}

	static sendXHR(method, url, headers, body, onResponseAvailable, onFailedResponse) {
		var xhr = RequestUtils.makeXHR(method, url, headers, body);
		xhr.onreadystatechange = function() {
			if (this.readyState == XMLHttpRequest.DONE) {
				if (this.status == 200) {
					onResponseAvailable(this.reponseText);
				} else {
					onFailedResponse(this.reponseText);
				}
			}
		}
		method = method.toLowerCase();
		if (method == 'get') {
			xhr.send();
		} else if (method == 'post') {
			xhr.send(body);
		}
	}

	/**/

	static makeFetch(method, url, headers, body) {
		console.log(body);
		method = method.toLowerCase();
		if (body != null && method == 'get') {
			if (!url.includes('?')) url += '?';
			for (var [name, value] of body.entries()) {
				if (!url.endsWith('?')) url += '&';
				url += name + '=' + value;
			}
		}
		var req = method == 'get' ? {method: method, headers: headers} : {method: method, headers: headers, body: body};

		console.log(url);

		return fetch(url, req);
	}

	static sendFetch(method, url, headers, body, onSuccess, onFail) {
		console.log('send fetch');
		
		RequestUtils.makeFetch(method, url, headers, body)
		.then(response => {
			return response.text();
		})
		.then(responseText => {
			onSuccess(responseText);
		})
		.catch(e => {
			onFail(e);
		});
	}

	/**/

	static send(method, url, headers, body, onSuccess, onFail) {
		if ('fetch' in window) {
			RequestUtils.sendFetch(method, url, headers, body, onSuccess, onFail);
		} else {
			RequestUtils.sendXHR(method, url, headers, body, onSuccess, onFail);
		}
	}

	/**/

	static sendFormXHR(form, headers, onSuccess, onFail) {
		var formData = new FormData(form);
		RequestUtils.sendXHR(form.method, form.action, headers, formData, onSuccess, onFail);
	}

	static sendFormFetch(form, headers, onSuccess, onFail) {
		var formData = new FormData(form);
		RequestUtils.sendFetch(form.method, form.action, headers, formData, onSuccess, onFail);
	}

	static sendForm(form, headers, onSuccess, onFail) {
		if ('fetch' in window) {
			RequestUtils.sendFormFetch(form, headers, onSuccess, onFail);
		} else {
			RequestUtils.sendFormXHR(form, headers, onSuccess, onFail);
		}
	}

	static ajaxFormSubmit(ev, headers, onSuccess, onFail) {
		console.log('ajaxFormSubmit');
		ev.preventDefault();
		RequestUtils.sendForm(ev.target, headers, onSuccess, onFail);
	}
}