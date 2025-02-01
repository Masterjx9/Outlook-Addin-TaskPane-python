/*
 * Copyright (c) Microsoft Corporation. All rights reserved. Licensed under the MIT license.
 * See LICENSE in the project root for license information.
 */

/* global document, Office */

Office.onReady((info) => {
  if (info.host === Office.HostType.Outlook) {
    document.getElementById("sideload-msg").style.display = "none";
    document.getElementById("app-body").style.display = "flex";
    document.getElementById("run").onclick = run;
  }
});

async function run() {
  const bootstrapAlertDiv = document.getElementById("alert");
  bootstrapAlertDiv.innerHTML = `
    <div class="alert alert-success alert-dismissible fade show" role="alert">
      The Button works!!
      <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>
  `;
  
  await new Promise(resolve => setTimeout(resolve, 4000));
  bootstrapAlertDiv.innerHTML = "";
}

