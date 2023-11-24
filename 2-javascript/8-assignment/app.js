const loadData = (id) => {
  // const searchText = document.getElementById("search-box").value;

  fetch(`https://openapi.programming-hero.com/api/videos/category/${id}`)
    .then((res) => res.json())
    // .then((data) => console.log(data.data));
    .then((data) => displayData(data.data));
};

const displayData = (data) => {
  // document.getElementById("total-meals").innerText = data.length;

  const mainContainer = document.getElementById("main-container");
  mainContainer.innerHTML = "";
  // mainContainer.innerHTML = `<h1 class="text-primary">Total: ${data.length}</h1>`;
  if (!data.length) {
    mainContainer.innerHTML = `
    <div class="mx-auto">
    <img src="./Icon.png" class="w-100 mt-4" /></div>
    
    `;
  }
  data.forEach((data) => {
    console.log(data);
    const icon = '<i class="ms-2 text-primary fa-regular fa-circle-check"></i>';
    const card = document.createElement("div");
    card.classList.add("col");
    card.innerHTML = `
    
    <div class="p-2 border bg-light">
    <img class="w-100 inner-image rounded-3" src=${data.thumbnail} alt="">
    <div class="row d-flex justify-content-center align-items-center mt-2">
      <div class="col-lg-3">
        <img src="${data.authors[0].profile_picture}" alt="" class="profile" />
      </div>
      <div class="col-lg-8 ms-4">
        <h6 class="">${data.title}</h6>
        <div class="d-flex justify-content-start align-items-center">
          <div><small class="text-secondary">${
            data.authors[0].profile_name
          }</small></div>
          <div id="v">
            ${data.authors[0].verified ? icon : ""}
          </div>
        </div>
        <small class="text-secondary">${data.others.views}</small>
      </div>
    </div>
    </div>
    

        
        
        `;

    mainContainer.appendChild(card);

    // if (data.authors[0].verified) {
    //   const v = document.getElementById("v");
    //   v.innerHTML = `<i class="ms-3 text-primary fa-regular fa-circle-check"></i>`;
    // }
  });
};

// loadData(1000);
