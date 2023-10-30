var tmp_obj = {"fulfilled":email_template_fulfilled,"placed":email_template_placed,"abandoned":email_template_abandoned}
let tmp_status = templates;

const tsel = document.getElementById('tempsel');

tsel.addEventListener('change', function (e) {
    let current_tmp = e.target.value
    CKEDITOR.instances['ckeditor'].setData(tmp_obj[current_tmp]);

    let status_e = document.getElementById("tempstatus")
    if (tmp_status[current_tmp] == parseInt(1)){
        status_e.textContent = "Enabled"
    }else{
        status_e.textContent = "Disabled"
    }

});


function prodapi(api,obj){
  fetch(api, {
    method: "POST",
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(obj)
  })
  .then((response) => response.json())
  .then((data) => {
    if (data.status == parseInt(1)){
        swal("Updated", data.message, "success");
    }else{
        swal("Update failed", data.message, "error");
    }
});
}

function loadtemp(){
    let dbobj = templates;
    let status_ = document.getElementById("tempstatus")
    let status = status_.textContent
}

function prodsettings_temp(){
    // CKEDITOR.instances['ckeditor'].setData(value);
    let dbobj = templates;
    let status_ = document.getElementById("tempstatus")
    let status = status_.textContent
    console.log(status)

    let ck = CKEDITOR.instances['ckeditor'].getData();
    console.log(ck)

}

function prodsettings_rates(){
    let status = document.getElementById("shipping")
    let selcountries = []
    let checkboxes = document.querySelectorAll('input[type=checkbox]:checked')
    for (var i = 0; i < checkboxes.length; i++) {
    selcountries.push(checkboxes[i].value)
    }
    prodapi("/api/prodset-ship",{"countries":selcountries,"shipping":JSON.stringify(shipping),"status":status.value})
}

function prodsettings_str(){
    let sk = document.getElementById("skey").value
    let pk = document.getElementById("pkey").value
    let wk = document.getElementById("wskey").value
    let ck = document.getElementById("ckey").value
    if (sk && pk && wk && ck){
        prodapi("/api/prodset-str",{"sk":sk,"pk":pk,"wsk":wk,"ck":ck})
    }else{
        swal("Stripe API", 'Missing information', "error");
    }
}

function prodsettings_smtp(){
}

