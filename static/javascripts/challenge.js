let datas = data
console.log(datas)
console.log(datas['question_count'])
console.log(datas['category'])
console.log(datas['difficulty'])
console.log(datas['type'])
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
    console.log(q_category,'q_category')
    console.log(q_difficulty,'q_difficulty')
    console.log(q_type,'q_type')
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

function get_id(ids){
    console.log(ids)
    if(ids=='option_1'||ids=='option_2'||ids=='option_3'||ids=='option_4'){
        
        for(let i= 0;i<=3;i++){
            
            if(ids!=`option_${i+1}`){
                console.log(ids,`option_${i+1}`,'white')
                $(`#option_${i+1}`).css("background-color",'white')
            }
            else{
                console.log(ids,`option_${i+1}`,'yellow')
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
    for(let i=0;i<=3;i++){
        $(`#option_${i+1}`).css("background-color",'white')
    }

    if(d[q_number]['type']=='boolean'){
        $(`#option_1_true`).css("background-color",'white')
        $(`#option_2_false`).css("background-color",'white')
        $('#multiple_choice').hide()
        $('#bool').show()
        $('#question_id_tag').html(d[q_number]['question'])
    }
    else{
        $('#multiple_choice').show()
        $('#bool').hide()
        console.log(d,q_number)
        let index = Math.floor(Math.random()*4)
        let opt_arr = d[q_number]['incorrect_answers']
        opt_arr.splice(index,0,d[q_number]['correct_answer'])
        console.log(opt_arr)
        $('#question_id_tag').html(d[q_number]['question']) 

        for(let i=0;i<opt_arr.length;i++){
            // $(`#option_${i+1}`).html(`${((i+10).toString(36)).toUpperCase()})  ${opt_arr[i]}`) 
            $(`#option_${i+1}`).html(`${opt_arr[i]}`)
            
    }
    }
    
    

}

$.ajax({
    type: 'GET',
    url: url_maker(),
    dataType: "json" ,
    success: function(question_set){
        // var q_set = question_set
        // console.log(question_set)
        var counts = 0
        $('#next_question').click(()=>{
            
            console.log('clicked')
            q_set(question_set['results'],counts)
            counts+=1
            
        })

        
    
        
    },
    error: function(){
        console.log('Page not found ')
    }
})


