var button = document.querySelector("#btn-slog");

function foo(event)
{
    element = event.target;

    if ( element.classList.contains('btn-primary') )
    {
        var new_class = 'btn-danger';
        var old_class = 'btn-info';
    }
    else {
        var new_class = 'btn-info';
        var old_class = 'btn-danger';
    }

    element.classList.remove(old_class);
    element.classList.add(new_class);
}

button.addEventListener('click', foo, false);

// ajax
$( document ).on('click', '#ajax-btn', function(event) {
   console.log('Ответ 1');
   $.ajax({
               url: '/testapp/update-token-ajax/',
               success: function (data) {
                   // data - ответ от сервера
                   console.log('Ответ 3')
                   console.log(data);
                   $('#token').html(data.key);
               },
           });
});