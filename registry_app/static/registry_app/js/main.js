function open_dialog(id_dialog){
    var dialog = document.getElementById(id_dialog);
    dialog.showModal();    
}

function open_waring_dialog(waring_text){
    var dialog = document.getElementById('waring-dialog');
    document.getElementById('waring-text').innerHTML = waring_text;
    dialog.showModal();    
}

function close_window(id_dialog){
    var dialog = document.getElementById(id_dialog);
    dialog.close();    
}
function add_prepations(){
    $.ajax({
        type: "GET",
        url: "../new_prepations/",
        data:{
            'name':document.getElementById('name').value,
            'type_prepations':document.getElementById('type_prepations').value,
            'maker':document.getElementById('maker').value,
            'form_release':document.getElementById('form_release').value,
        },
        dataType: "html",
        cache: false,
        success: function(data){
            if (data == 'ok'){
                location.reload();
            }
            else if(data='repit_polis'){
                waring_text = 'Пользователь с таким полисом уже существует';
                open_waring_dialog(waring_text);
            }
        }
   });
}

function add_patient(){
    $.ajax({
        type: "GET",
        url: "../new_patient/",
        data:{
            'name':document.getElementById('name_patient').value,
            'lastname':document.getElementById('lastname').value,
            'patronymic':document.getElementById('patronymic').value,
            'address':document.getElementById('address').value,
            'polis':document.getElementById('polis').value,
            'phone':document.getElementById('phone').value,
            'date_of_birth':document.getElementById('date_of_birth').value,
            'sector':document.getElementById('sector').value,
            'Recording_date':document.getElementById('Recording_date').value,
        },
        dataType: "html",
        cache: false,
        success: function(data){
            if (data == 'ok'){
                location.reload();
            }
            else if(data='repit_polis'){
                waring_text = 'Пользователь с таким полисом уже существует';
                open_waring_dialog(waring_text);
            }
        }
   });
}


function after_downloading() {
    document.getElementById('name_patient').onfocus = function(){
        if (this.value == 'Имя пациента') {
            this.value = '';
            this.style.color = 'black';
        }
    }
    document.getElementById('name_patient').onblur = function(){
        if (this.value == '') {
            this.value = 'Имя пациента';
            this.style.color = '#b1afaf';
        }
    }

    document.getElementById('password').onfocus = function(){
        if (this.value == 'Пароль') {
            this.value = '';
            this.style.color = 'black';
        }
    }
    document.getElementById('password').onblur = function(){
        if (this.value == '') {
            this.value = 'Пароль';
            this.style.color = '#b1afaf';
        }
    }

    document.getElementById('re-password').onfocus = function(){
        if (this.value == 'Повторите пароль') {
            this.value = '';
            this.style.color = 'black';
        }
    }
    document.getElementById('re-password').onblur = function(){
        if (this.value == '') {
            this.value = 'Повторите пароль';
            this.style.color = '#b1afaf';
        }
    }

    document.getElementById('name_employee').onfocus = function(){
        if (this.value == 'Имя') {
            this.value = '';
            this.style.color = 'black';
        }
    }
    document.getElementById('name_employee').onblur = function(){
        if (this.value == '') {
            this.value = 'Имя';
            this.style.color = '#b1afaf';
        }
    }

    document.getElementById('last_name_employee').onfocus = function(){
        if (this.value == 'Фамилия') {
            this.value = '';
            this.style.color = 'black';
        }
    }
    document.getElementById('last_name_employee').onblur = function(){
        if (this.value == '') {
            this.value = 'Фамилия';
            this.style.color = '#b1afaf';
        }
    }

    document.getElementById('phone').onfocus = function(){
        if (this.value == 'Телефон') {
            this.value = '';
            this.style.color = 'black';
        }
    }
    document.getElementById('phone').onblur = function(){
        if (this.value == '') {
            this.value = 'Телефон';
            this.style.color = '#b1afaf';
        }
    }

    document.getElementById('address').onfocus = function(){
        if (this.value == 'Адрес') {
            this.value = '';
            this.style.color = 'black';
        }
    }
    document.getElementById('address').onblur = function(){
        if (this.value == '') {
            this.value = 'Адрес';
            this.style.color = '#b1afaf';
        }
    }

    document.getElementById('passport').onfocus = function(){
        if (this.value == 'Серия и номер паспорта') {
            this.value = '';
            this.style.color = 'black';
        }
    }
    document.getElementById('passport').onblur = function(){
        if (this.value == '') {
            this.value = 'Серия и номер паспорта';
            this.style.color = '#b1afaf';
        }
    }


    document.getElementById('post').onfocus = function(){
        this.style.color = 'black';
    }
    document.getElementById('post').onblur = function(){
        var numOption = document.getElementById("post").options.selectedIndex;
        if (numOption == 0) {
            this.style.color = '#b1afaf';
        }
    }

    document.getElementById('specialization').onfocus = function(){
        this.style.color = 'black';
    }
    document.getElementById('specialization').onblur = function(){
        var numOption = document.getElementById("specialization").options.selectedIndex;
        if (numOption == 0) {
            this.style.color = '#b1afaf';
        }
    }

    document.getElementById('type-users').onfocus = function(){
        this.style.color = 'black';
    }
    document.getElementById('type-users').onblur = function(){
        var numOption = document.getElementById("type-users").options.selectedIndex;
        if (numOption == 0) {
            this.style.color = '#b1afaf';
        }
    }

    
    document.getElementById('search-input').onfocus = function(){
        if (this.value == 'Поиск') {
            this.value = '';
            this.style.color = 'black';
        }
    }
    document.getElementById('search-input').onblur = function(){
        if (this.value == '') {
            this.value = 'Поиск';
            this.style.color = '#b1afaf';
        }
    }

    // search-button



    function search_preparations_reg(){
        var qwery = 'http://127.0.0.1:8000/registry/preparations/search?search_term=';
        qwery+=document.getElementById('search-input-preparations-reg').value;
        location.replace(qwery);
    }
    
    function search_patients(){
        var qwery = 'http://127.0.0.1:8000/registry/patients/search?search_term=';
        qwery+=document.getElementById('search-input-patients').value;
        location.replace(qwery);
    }
    

    document.getElementById('search-input').onfocus = function(){
        if (this.value == 'Поиск') {
            this.value = '';
            this.style.color = 'black';
        }
    }
    document.getElementById('search-input').onblur = function(){
        if (this.value == '') {
            this.value = 'Поиск';
            this.style.color = '#b1afaf';
        }
    }


    document.getElementById('search-input-prepations').onfocus = function(){
        if (this.value == 'Поиск') {
            this.value = '';
            this.style.color = 'black';
        }
    }
    document.getElementById('search-input-prepations').onblur = function(){
        if (this.value == '') {
            this.value = 'Поиск';
            this.style.color = '#b1afaf';
        }
    }


    document.getElementById('search-input-patients').onfocus = function(){
        if (this.value == 'Поиск') {
            this.value = '';
            this.style.color = 'black';
        }
    }
    document.getElementById('search-input-patients').onblur = function(){
        if (this.value == '') {
            this.value = 'Поиск';
            this.style.color = '#b1afaf';
        }
    }

    document.getElementById('search-input-recepts').onfocus = function(){
        if (this.value == 'Поиск') {
            this.value = '';
            this.style.color = 'black';
        }
    }
    document.getElementById('search-input-recepts').onblur = function(){
        if (this.value == '') {
            this.value = 'Поиск';
            this.style.color = '#b1afaf';
        }
    }
    
}