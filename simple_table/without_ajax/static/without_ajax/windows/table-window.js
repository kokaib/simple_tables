class TableWindow extends Window {

    // can't use 'tableWindow' if it's called from a fetch promise...
    // TODO: return instances of tableWindow class from a static/global method (?)
    //       or get rid of the class encapsulation entirely

    /*  */

    onResponseAvailable(response) {
        console.log('response');
        /*
        Response is in the following format:

            {
                "request_get": "...",
                "is_successful": 0/1,
                "response_text": "..."
            }

        */

        var requestGET = response['request_get'];
        var isSuccessful = response['is_successful'];
        var responseText = response['response_text'];

        if (isSuccessful) {
            tableWindow.onTableResponse(requestGET, responseText);
        } else {
            tableWindow.onFormResponse(responseText);
        }
    }


    /*  */
    
    onTableResponse(requestGET, responseText) {
        console.log('table response');

        popup.removeInstance();

        var elem = document.querySelector('#table-container');
        elem.innerHTML = responseText;

        tableWindow._queryStringState.state = requestGET;
    }

    onFormResponse(responseText) {
        console.log('form response');

        popup.appendInstance();

        var elem = popup.instance.querySelector('.content');
        elem.innerHTML = responseText;

        var headers = {  }

        var form = elem.querySelector('form');

        if (form.method.toLowerCase() === 'post') {
            var csrftoken = Cookies.getCookie('csrftoken');
            headers = {
                'X-CSRFToken': csrftoken,
                'X-Requested-With': 'XMLHttpRequest'
            }
        }

        form.addEventListener('submit', ev => {
            form.action = tableWindow._queryStringState.attachState(form.action);
            RequestUtils.ajaxFormSubmit(
                ev,
                headers,
                windowDispatcher.onResponseAvailable,
                windowDispatcher.onResponseFailed
            );
        }, false);
    }


    /* add-update */

    startAdd() {
        var headers = {  };
        RequestUtils.send(
            'get',
            `add/`,
            headers,
            null,
            windowDispatcher.onResponseAvailable,
            windowDispatcher.onResponseFailed
        );
    }

    startUpdate(ev) {
        var id = ev.target.closest('tr').id;
        var headers = {  };
        RequestUtils.send(
            'get',
            `update/${id}`,
            headers,
            null,
            windowDispatcher.onResponseAvailable,
            windowDispatcher.onResponseFailed
        );
    }


    /* filters */

    filterColumnCategorical(ev) {
        var id = ev.target.id;
        var headers = {  };
        RequestUtils.send(
            'get',
            tableWindow._queryStringState.attachState(`filter-categorical/Model2/${id}`),
            headers,
            null,
            windowDispatcher.onResponseAvailable,
            windowDispatcher.onResponseFailed
        );
    }

    filterColumnRangeNumber(ev) {
        var id = ev.target.id;
        var headers = {  };
        RequestUtils.send(
            'get',
            tableWindow._queryStringState.attachState(`filter-range-number/Model2/${id}`),
            headers,
            null,
            windowDispatcher.onResponseAvailable,
            windowDispatcher.onResponseFailed
        );
    }

    filterColumnRangeDate(ev) {
        var id = ev.target.id;
        var headers = {  };
        RequestUtils.send(
            'get',
            tableWindow._queryStringState.attachState(`filter-range-date/Model2/${id}`),
            headers,
            null,
            windowDispatcher.onResponseAvailable,
            windowDispatcher.onResponseFailed
        );
    }


    /* paging */

    pageTo(n) {
        RequestUtils.send(
            'get',
            tableWindow._queryStringState.attachState(`table?page=${n}`),
            headers,
            null,
            windowDispatcher.onResponseAvailable,
            windowDispatcher.onResponseFailed
        );
    }
}