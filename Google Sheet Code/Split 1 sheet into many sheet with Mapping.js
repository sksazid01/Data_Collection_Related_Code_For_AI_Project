function splitSheetIntoChunksWithColors() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sourceSheet = ss.getActiveSheet();
  var data = sourceSheet.getDataRange().getValues();
  var colors = sourceSheet.getDataRange().getBackgrounds();
  var numRows = data.length;
  var chunkSize = 2; // Number of rows per new sheet
  var numChunks = Math.ceil(numRows / chunkSize);

  for (var i = 0; i < numChunks; i++) {
    var startRow = i * chunkSize;
    var endRow = Math.min(startRow + chunkSize, numRows);
    var chunkData = data.slice(startRow, endRow);
    var chunkColors = colors.slice(startRow, endRow);

    // Create a new sheet for each chunk
    var newSheet = ss.insertSheet('ds' + (i + 1));
    newSheet.getRange(1, 1, chunkData.length, chunkData[0].length).setValues(chunkData);
    newSheet.getRange(1, 1, chunkColors.length, chunkColors[0].length).setBackgrounds(chunkColors);
  }
}

function onEdit(e) {
  var editedSheet = e.source.getActiveSheet();
  var sheetName = editedSheet.getName();

  // Check if the edited sheet is one of the ds sheets
  if (sheetName.startsWith('ds')) {
    var row = e.range.getRow();
    var col = e.range.getColumn();

    // Check if the edited cell is in column C
    if (col === 3) {
      var mainSheet = e.source.getSheets()[0]; // Assuming the main sheet is the first sheet
      var chunkNumber = parseInt(sheetName.substring(2), 10);
      var mainSheetRow = (chunkNumber - 1) * 2 + row; // Calculate the corresponding row in the main sheet
      mainSheet.getRange(mainSheetRow, 3).setValue(e.value);
    }
  }
}
