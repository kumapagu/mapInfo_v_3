import { CSRF_TOKEN } from "./csrf_token.js";

function handleResponse(response) {
    if (response.status === 204) {
        return ""
    } else if (response.status === 404) {
        return null
    } else {
        return response.json()
    }
}

function apiService(endpoint, method, data) {
    let config
    if (method == 'POST' || method == 'PUT') {
        const formData = new FormData()
        Object.keys(data).forEach((key) => {
        formData.append(key, data[key])
        })
        config = {
            method: method,
            body: formData,
            headers: {
                "X-CSRFTOKEN": CSRF_TOKEN
            }
        };
    }else{
        config = {
            method: method,
            headers: {
                "X-CSRFTOKEN": CSRF_TOKEN
            }
        };
    }
    return fetch(endpoint, config).then(handleResponse)
}

export { apiService }