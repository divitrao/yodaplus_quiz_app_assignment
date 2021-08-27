let datas = data
// console.log(datas)
// console.log(datas['question_count'])
// console.log(datas['category'])
// console.log(datas['difficulty'])
// console.log(datas['type'])
let q_counts = datas['question_count']
let q_category = datas['category']
let q_difficulty = datas['difficulty']
let q_type = datas['type']

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






function url_maker(){
    // console.log(q_category,'q_category')
    // console.log(q_difficulty,'q_difficulty')
    // console.log(q_type,'q_type')
    if(q_category=='any'){
        q_category =0
    }
    if(q_difficulty=='any'){
        q_difficulty =0
    }
    if(q_type=='any'){
        q_type =0
    }
    // console.log(`https://opentdb.com/api.php?amount=${q_counts}&category=${q_category}&difficulty=${q_difficulty}&type=${q_type}`)
    return `https://opentdb.com/api.php?amount=${q_counts}&category=${q_category}&difficulty=${q_difficulty}&type=${q_type}`
}

var id_arr = []
var total_score = 0
var correct_answer 
var arr_for_bool = []
var bool_answer
$('#lock').click(function(){
    $('#main_div').addClass('disable_div')
    $("#lock").prop('disabled', true)
    console.log(id_arr[0],' corect one is ',correct_answer)
    if(arr_for_bool.length>0){
        if(id_arr[0]=='option_1_true'){
             bool_answer = 'True'
        }
        else{
            bool_answer = 'False'
        }
        if(bool_answer==correct_answer){
            total_score+=1
        }
        else{
            total_score-=1
        }
        console.log(total_score)
    }
    else{
        
        
        if(id_arr[0]==correct_answer){
            total_score+=1
        }
        else{
            total_score-=1
        }
        // console.log(d,q_number)
        console.log(id_arr[0])
        console.log('total score is ',total_score)
    }
    
})

function get_id(ids){
    $("#lock").prop('disabled', false);
    // console.log(ids)
    id_arr.pop()
    id_arr.push(ids)
    if(ids=='option_1'||ids=='option_2'||ids=='option_3'||ids=='option_4'){
        
        for(let i= 0;i<=3;i++){
            
            if(ids!=`option_${i+1}`){
                // console.log(ids,`option_${i+1}`,'white')
                $(`#option_${i+1}`).css("background-color",'white')
            }
            else{
                // console.log(ids,`option_${i+1}`,'yellow')
                $(`#${ids}`).css("background-color",'rgba(255,204,0)')
            }
        }
    }
    else{
        if(ids=='option_1_true'){
            $(`#option_1_true`).css("background-color",'rgba(255,204,0)')
            $(`#option_2_false`).css("background-color",'white')
        }
        else{
            $(`#option_1_true`).css("background-color",'white')
            $(`#option_2_false`).css("background-color",'rgba(255,204,0)')
        }
    }
    // // console.log("Background color = " + $(`#${ids}`).css("background-color"))
    // $(`#${ids}`).css("background-color",'rgba(255,204,0)') 
    // for(j=0;j<)
}

function q_set(d,q_number=0){
    document.querySelector("#main_div").classList.remove('disable_div');
    $("#lock").prop('disabled', true);
    for(let i=0;i<=3;i++){
        $(`#option_${i+1}`).css("background-color",'white')
    }

    if(d[q_number]['type']=='boolean'){
        $(`#option_1_true`).css("background-color",'white')
        $(`#option_2_false`).css("background-color",'white')
        $('#multiple_choice').hide()
        $('#bool').show()
        correct_answer = d[q_number]['correct_answer']
        arr_for_bool.splice(0,arr_for_bool.length)
        arr_for_bool.push(d[q_number]['correct_answer'],d[q_number]['incorrect_answers'][0])
        $('#question_id_tag').html(`${q_number + 1 }) ${d[q_number]['question']}`)
        console.log(arr_for_bool)
    }
    else{
        $('#multiple_choice').show()
        $('#bool').hide()
        arr_for_bool.splice(0,arr_for_bool.length)
        console.log(d,q_number)
        let index = Math.floor(Math.random()*4)
        let opt_arr = d[q_number]['incorrect_answers']
        opt_arr.splice(index,0,d[q_number]['correct_answer'])
        correct_answer = `option_${index+1}`
        console.log(opt_arr)
        $('#question_id_tag').html(`${q_number+ 1}) ${d[q_number]['question']}`) 

        for(let i=0;i<opt_arr.length;i++){
            // $(`#option_${i+1}`).html(`${((i+10).toString(36)).toUpperCase()})  ${opt_arr[i]}`) 
            $(`#option_${i+1}`).html(`${opt_arr[i]}`)
            
    }
    }
    // console.log(id_arr[0],' corect one is ',correct_answer)
    

}

$.ajax({
    type: 'GET',
    url: url_maker(),
    dataType: "json" ,
    success: function(question_set){
        q_set(question_set['results'])
        // var q_set = question_set
        // console.log(question_set)
        var counts = 0
        // console.log(question_set)
        $('#next_question').click(()=>{
            counts+=1
            if(counts>=datas['question_count']){
                // console.log('larger alert')
                $('#score').attr('href',`score/${total_score}`)
            }
            else{
                // console.log('clicked')
                q_set(question_set['results'],counts)
                if(counts==datas['question_count']-1){
                    $('#next_question').html('CHECK SCORE')
                }
                // console.log(counts,'counts are')
            }
            
            
            
        })

        
    
        
    },
    error: function(){
        console.log('Page not found ')
    }
})


