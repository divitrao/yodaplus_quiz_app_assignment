// console.log('hi')
// console.log($('#stopwatch').html())

// var data = JSON.parse("{{data|escapejs}}");
console.log(data)
function start_time(second){
    
    

var interval_id = window.setInterval(function(){
    $('#stopwatch').html(second--)

    $('#next_question').click(function(){
        clearInterval(interval_id)
        start_time(60)
    })

    if(second==1){
        $('#stopwatch').html('Time out ')
        clearInterval(interval_id)
    } 
},1000)
}

// start_time(60)


