const max_description_value = 75

function to_title_case(str)
{
    return str.replace(/\w\S*/g, function(txt){
        return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
    });
}

function convert_to_list_table(data, valid_headers) {
    headers = []
    table = ''
    if(data.length > 0) {
        table += '<tr>\n'
        for(var i=0;i<valid_headers.length;i++){
            let key = valid_headers[i];
            headers.push();
            let display_key = to_title_case(key.replace("_", " "));
            table += `<th class="${key}">${display_key}</th class="${key}">\n`;
        }
        table += '</tr>\n'
    } else {
        throw new RangeError("Data list must have at least one element")
    }
    // Construct table
    for(var i=0; i<data.length; i++) {
        // construct row
        row = ''
        id = data[i]['id']
        for(var j=0; j<valid_headers.length; j++) {
            let key = valid_headers[j]
            if(key=='Poster') {
                value = `<img class="movie-mini-poster" src="${data[i][key]}"></img>`;
            } else {
                value = data[i][key];
            }
            row += `<td id="${id}" class="${key}">${value}</td>\n`
        }
        table += `<tr class="clickable-data-row" data-href='/movies/${id}'>\n` + row + '</tr>\n'
    }
    return table
}

function buttonConfirm(action){
    if (window.confirm("Are you sure?")) {
        action()
    }
};

function success(message){
    var div = document.createElement("div");
    div.setAttribute('id', 'media-message')
    div.style.width = '0px';
    div.style.height = '80px';
    div.style.position = 'absolute';
    div.style.borderRadius = '10px';
    // div.style.border = '2px solid black';
    div.style.background = '#55CC55';
    div.style.innerHTML = 'BLAHBLAHBLAH';
    div.style.left = '0em';
    div.style.top = '20em';

    document.body.append(div);
    setTimeout(function(){
        mb = $('#media-message')
        document.getElementById('media-message').style.border = '2px solid black';
        mb.animate({'width': 250});
        mb.animate({'left': '+=30'}, speed=125);
    }, 1000);
    setTimeout(function(){
        mb = $('#media-message')
        mb.animate({'width': 0});
        mb.animate({'left': '-=30'}, speed=125, callback=function(){
            document.getElementById('media-message').style.border = null;
        });
    }, 3000)

    // console.log(

    // div.animate({
    //     'width': '250px'
    // })
}