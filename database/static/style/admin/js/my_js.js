
function couponHide(type) {
    let block = document.getElementById("option_1");
    if (type === 1) {
        block.style.display = "block";
    } else {
        block.style.display = "none";
    }
}

function activityImage(option) {
    let div_url = document.getElementById("div_url");
    let div_upload = document.getElementById("div_upload");
    if (option === 1) {
        div_url.style.display = "block";
        div_upload.style.display = "none";
    } else {
        div_url.style.display = "none";
        div_upload.style.display = "block";
    }
}