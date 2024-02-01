var depoLog = [];

function logg() {
  // var ll = "";
  const logContainer = document.getElementById("log");
  for (var i = 0; i < depoLog.length; i++) {
    // ll.concat(depoLog[i], ",<br>");
    // depoLog.join(' ');
    // ll += i + 1 + ". " + depoLog[i] + " ";
    // document.getElementById("log").innerText = ll;
    const h1 = document.createElement("h1");
    h1.classList.add("text-start", "ps-5", "text-danger");
    h1.innerText = i + 1 + ". " + depoLog[i];
    logContainer.appendChild(h1);
  }
  // document.getElementById("log").innerText = ll;
}

function depo() {
  var iv = document.getElementById("depo_in").value;

  var dAmount = document.getElementById("depo_amount").innerText;
  var totalAmount = document.getElementById("total").innerText;
  // console.log(dAmount);
  document.getElementById("depo_amount").innerText =
    parseInt(iv) + parseInt(dAmount);

  // console.log("Deposited successfully!", { iv });

  document.getElementById("total").innerText =
    parseInt(iv) + parseInt(totalAmount);
  document.getElementById("depo_in").value = "";

  depoLog.unshift(`Deposited $${iv} successfully`);
  document.getElementById(
    "update"
  ).innerText = `Deposited $${iv} successfully!`;
  // log();
  // document.getElementById("log").innerText = log();
  // for (var i = 0; i < depoLog.length; i++) {
  //   document.getElementById("log").innerText = depoLog[i];
  // }
  // console.log(" ");
}

function withdraw() {
  var iv = document.getElementById("with_in").value;

  var dAmount = document.getElementById("withdraw").innerText;

  var totalAmount = document.getElementById("total").innerText;

  if (parseInt(totalAmount) < parseInt(iv)) {
    alert("Low balance!");
    return;
  }
  document.getElementById("withdraw").innerText =
    parseInt(iv) + parseInt(dAmount);

  document.getElementById("total").innerText =
    parseInt(totalAmount) - parseInt(iv);
  document.getElementById("with_in").value = "";

  document.getElementById("update").innerText = `Withdrew $${iv} successfully!`;
  depoLog.unshift(`Withdrew $${iv} successfully`);

  // console.log("All Logg");
  // for (var i = 0; i < depoLog.length; i++) {
  //   console.log(depoLog[i]);
  // }
  // console.log(" ");
}
