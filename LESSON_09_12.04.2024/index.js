const xhr = new XMLHttpRequest()

let api_request_method = 'GET'
let api_server_url = 'https://api.github.com/users/dan'

xhr.open(api_request_method, api_server_url)

xhr.onload = () => {
    console.log(xhr)
    console.log(xhr.responseText)
}

xhr.send()

