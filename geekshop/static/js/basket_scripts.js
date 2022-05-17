window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function (event) {
        var input_element = event.target;

        fetch(`/basket/edit/${input_element.name}/${input_element.value}/`).then(
            function (response) {
                return response.body;
            }).then(function(body) {
                $('.basket_list').html(body);
            })
        event.preventDefault();
    });
}
