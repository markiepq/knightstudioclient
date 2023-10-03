let on = 'margin-top:5px;background-color:mediumseagreen;color:white';
let off = 'margin-top:5px;background-color:black;color:white';
var product_data = {
  "id": GenID(),
  "title": "",
  "category": "",
  "variants": {},
  "product_url": "",
  "seo_description": "",
  "seo_keywords": "",
  "images": [],
  "mainimage": "",
  "body":"",
  "price":"",
  "variant_details":{},
};
var variant_data = [];
var variant_data_dict = {};
var variant_data_history = {};
var images = [];

function AutoOff() {

}

function GenID() {
  return Math.floor(Math.random() * Date.now())
}

function fname(len) {
  let text = "";

  var charset = "abcdefghijklmnopqrstuvwxyz0123456789";

  for (var i = 0; i < len; i++)
    text += charset.charAt(Math.floor(Math.random() * charset.length));

  return text;
}


function knightapi(data) {
  fetch("/knightclientapi", {
    method: "POST",
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  }).then(res => {
    swal("Logs deleted", 'Please refresh page', "success");
    //console.log("Request complete! response:", res);
  });
}


function knightapi2(data) {
  var hb = document.getElementById("hb2")
  if (hb.innerText == 'Hide post') {
    hb.innerText = 'Unhide post';
    data = {
      "action": "blog_1",
      "where": data
    }
    fetch("/knightclientapiv2", {
      method: "POST",
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    }).then(res => {

      swal("Updated", 'Blog post updated', "success");
      document.getElementById("ishidden").value = "1"
      //console.log("Request complete! response:", res);
    });
  } else {
    hb.innerText = 'Hide post';
    data = {
      "action": "blog_0",
      "where": data
    }
    fetch("/knightclientapiv2", {
      method: "POST",
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    }).then(res => {

      swal("Updated", 'Blog post updated', "success");
      document.getElementById("ishidden").value = "0"

      //console.log("Request complete! response:", res);
    });
  }
}

function confirm_dedit(key, route) {
  var id = "finald"
  var d = document.getElementById(id).style.display;
  if (d == "none") {
    document.getElementById(id).style.display = "inline-block";
  } else {
    document.getElementById(id).style.display = "none";
  }
}


function confirm_d(key, route, id) {
  var d = document.getElementById(id).style.display;
  if (d == "none") {
    document.getElementById(id).style.display = "block";
  } else {
    document.getElementById(id).style.display = "none";
  }
}

function deleapip(d, b, id) {
  var o = {
    "1": {
      "table": "products",
      "column": "product_urlsystem",
      "value": b
    }
  }

  fetch("/deleapip", {
    method: "POST",
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(o[d])
  }).then(res => {
    if (id === "9999") {
      location.href = "/product-manage/1";
    } else {
      document.getElementById('tr-' + id).remove();
      swal("Product manager", 'Product deleted', "success");
    }


    //console.log("Request complete! response:", res);
  });
}


function deleapi(d, b, id) {
  var o = {
    "1": {
      "table": "blog",
      "column": "route",
      "value": b
    }
  }
  fetch("/deleapi", {
    method: "POST",
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(o[d])
  }).then(res => {
    if (id === "9999") {
      location.href = "/blog-manage/1";
    } else {
      document.getElementById('tr-' + id).remove();
      swal("Blog manager", 'Blog post deleted', "success");
    }


    //console.log("Request complete! response:", res);
  });
}



function updateMod(which, OnOrOff) {

  let data = {};

  if (which == "announcement") {
    v = document.getElementById('announcement_content').value
    if (v) { // process here
      data.module = which;
      data.enabled = OnOrOff;
      data.message = v;
    } else {
      return false
    }
  } else if (which == "popup") {
    im = document.getElementById('popup_img').value
    ms = document.getElementById('popup_message').value
    if (im || ms) { // process here
      data.module = which;
      data.enabled = OnOrOff;
      data.image = im;
      data.message = ms;
    } else {
      return false
    }
  } else if (which == "uparrow") {
    cl = document.getElementById('uparrow_content').value
    if (cl) { // process here
      data.module = which;
      data.enabled = OnOrOff;
      data.color = cl;
    } else {
      return false
    }
  } else if (which == "socialshare") {
    fb = document.getElementById('socialshare_facebook').value;
    ig = document.getElementById('socialshare_instagram').value;
    tw = document.getElementById('socialshare_twitter').value;
    gl = document.getElementById('socialshare_google').value;
    if (fb || ig || tw || gl) { // process here
      data.module = which;
      data.enabled = OnOrOff;
      data.fb = fb;
      data.ig = ig;
      data.tw = tw;
      data.gl = gl;
    } else {
      return false
    }
  } else if (which == "videoembed") {
    cls = document.getElementById('videoembed_code').value
    cls_t = document.getElementById('videoembed_thumbnail').value
    if (cls && cls_t) { // process here
      data.module = which;
      data.enabled = OnOrOff;
      data.code = cls;
      data.thumbnail = cls_t;
    } else {
      return false
    }
  } else if (which == "custom") {
    clss = document.getElementById('custom_code').value
    if (clss) { // process here
      data.module = which;
      data.enabled = OnOrOff;
      data.code = clss;
    } else {
      return false
    }
  } else if (which == "extras") {
    extras_whatsapp = document.getElementById('extras_whatsapp').value
    extras_number = document.getElementById('extras_number').value
    extras_email = document.getElementById('extras_email').value
    extras_address = document.getElementById('extras_address').value
    if (extras_whatsapp || extras_number || extras_email || extras_address) { // process here
      data.module = which;
      data.enabled = OnOrOff;
      data.whatsapp = extras_whatsapp;
      data.number = extras_number;
      data.email = extras_email;
      data.address = extras_address;
    } else {
      return false
    }
  }


  fetch("/module_update", {
    method: "POST",
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  }).then(res => {
    swal("", 'Module Updated', "success");
    //console.log("Request complete! response:", res);
  });
  return true
}

function OnOff(which) {
  var mod = document.getElementById(which + "_btn");
  if (mod.textContent === "On") { // Turn OFF
    if (updateMod(which, 0)) {
      mod.textContent = "Off";
      mod.style = off
    }

  } else { // Turn ON
    if (updateMod(which, 1)) {
      mod.textContent = "On";
      mod.style = on
    }
  }

}

function p_update(v) {
  swal("", 'Variant name required', "error");
}

function p_variant_add(e) {
  var cont_v = document.getElementById('v-title').value;
  document.getElementById("current-var")
  if (cont_v.length === 0) {
    swal("", 'Variant name characters not enough', "error");
    return false;
  }

  if (variant_data.includes(cont_v + "-ivar")) {
    swal("", 'Variant name Exists', "error");
    return false;
  }

  var cont_vid = cont_v.replace(/[^A-Z0-9]+/ig, "-");
  var newRow = document.getElementById('variant-table').insertRow();
  document.getElementById('variant-notice').style.display = "none";
  var varid = cont_v + "-ivar"
  newRow.innerHTML = "<tbody>\
    <tr>\
    <td id='td-" + cont_v + "'><b><center><p class='text-dark rounded'>" + cont_v + "</p></center></b></td> <td class='col-1'><input type='number' class='form-control' id='" + cont_v + "-price' placeholder='This variant's price' value='1.00' style='width:80px;padding:0'></input></td><td class='col-1'><input type='number' class='form-control' id='" + cont_v + "-stock' placeholder='How much stock you have' value='1000' style='width:80px;padding:0'></td> <td id='img-" + cont_v + "' class='col-4'><form enctype='multipart/form-data'><input type='file' name='" + varid + "' id='" + varid + "'></form></td><td><button type='button' id='btnd-" + cont_v + "' onclick='p_del(this)' class='btn btn-xs border col-xs-1'>X</button>&nbsp&nbsp</td>\
    </tr>\
    </tbody><br>";
  document.getElementById('v-title').value = "";
  const inputElementvar = document.querySelector(`#` + varid);
  p = FilePond.create(inputElementvar, {
    server: './upload-p-variant',
    credits: false,
    labelIdle: "Drop or Browse..",
    fileMetadataObject: {
      p_id: product_data['id'],
      p_variant: cont_v,
    },
    fileRenameFunction: (file) => {
      return fname(19)+`${file.extension}`;
    }


  }); //pondvar ends

  variant_data.push(varid);
  p.on('addfile', (error, file) => {
    // this object contains the file info
    variant_data_history[cont_v + "-ivar"] = file.file.name
    // file.file.filename = "asdasdasd"
  })
}



function p_updatevariant(ids) {
  let pr = document.getElementById(ids + "-price").value;
}

function p_set_settings(dom) {
  let n = document.getElementById(dom).value;
  if (!n) {
    swal("", 'Value required', "error");
    return false;
  } else {

    if (dom === 'p-desc') {
      product_data['seo_description'] = n;
    } else {
      product_data['seo_keywords'] = n;
    }
  }

  console.log(product_data)
}


function p_del(r) {
  let i = r.parentNode.parentNode.rowIndex;
  let l = document.getElementById("variant-table").rows.length;
  let b = r.id.replace("btnd-", "")
  document.getElementById("variant-table").deleteRow(i);

  // server side del
  try{
  const dt = { data: { fid : product_data['id'], filev : variant_data_history[b+"-ivar"]}};
  const request = axios.delete("/upload-p-variant", dt);
      }catch{
        console.log("unable to delete on backend")
      }


  // server side del

  if (variant_data.length - 1 <= 0) {
    document.getElementById('variant-notice').style.display = "block";
  }
  variant_data = variant_data.filter(v => v !== b + "-ivar");

  if (b + "-ivar" in variant_data_dict) {
    delete variant_data_dict[b + "-ivar"];
  }

}

function validatePrice(input) {
  const regex = new RegExp(/^\$?(?:(?:\d+(?:,\d+)?(?:\.\d+)?)|(?:\.\d+))$/);
  return regex.test(input);
}

function grabvariantdata(){
  var vardata = {};
  for (let i = 0; i < variant_data.length; i++) {
      var _p = document.getElementById(variant_data[i].replace("-ivar","")+"-price").value
      var _s = document.getElementById(variant_data[i].replace("-ivar","")+"-stock").value

      if (!validatePrice(_p)){
          swal("", 'Price not accepted, unable to validate', "error");
          return false;
      }
      if (!validatePrice(_s)){
          swal("", 'Stocks not accepted, unable to validate', "error");
          return false;
      }

      vardata[variant_data[i]] = {'price':_p , 'instock':_s};
      product_data['variant_details'] = vardata;
  }
}

function grabinputs(){
  product_data['images'] = images;
  product_data['title'] = document.getElementById("title").value;
  product_data['price'] = document.getElementById("m-price").value;
  product_data['category'] = document.getElementById("categ").value;
  product_data['product_url'] = document.getElementById("p-url").value;
  product_data['seo_description'] = document.getElementById("p-desc").value;
  product_data['seo_keywords'] = document.getElementById("p-keywords").value;
  product_data['body'] = CKEDITOR.instances['ckeditor'].getData();
  // product_data['images'] = categorydocument.getElementById("categ").value;
  // product_data['mainimage'] = categorydocument.getElementById("categ").value;
  if (product_data['title'].length <= 4 ){
      swal("", 'Failed validating title, must contain 5 or more characters', "error");
      return false;
  }
  // if (product_data['product_url'].length <= 4 ){
  //     swal("", 'URL must contain 10 or more characters, or leave blank', "error");
  //     return false;
  // }
  if (product_data['body'].length <= 4 ){
      swal("", 'Product description must have 5 or more characters', "error");
      return false;
  }
  if (product_data['price'].length <= 0 ){
          swal("", 'Price not accepted, unable to validate', "error");
      return false;
  }
  if (!validatePrice(product_data['price'])){
      swal("", 'Price not accepted, unable to validate', "error");
      return false;

  }
  grabvariantdata()
}


function build_variants() {
  grabinputs();
  for (let i = 0; i < variant_data.length; i++) {
    variant_data_dict[variant_data[i]] = document.getElementsByName(variant_data[i])[0].value
  }
  product_data['variants'] = variant_data_dict
}

function p_publish() {
  // document.getElementById("loading").style = 'display:block';
  // document.getElementById("publishb").style = 'display:none';
  build_variants()
  fetch("/product-publish", {
    method: "POST",
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(product_data)
    }).then(res => {
    // swal("", 'Module Updated', "success");
    console.log("Request complete! response:", res);
  });

}
window.onbeforeunload = function() {
  return "Leaving this page will not save your product information.";
}
