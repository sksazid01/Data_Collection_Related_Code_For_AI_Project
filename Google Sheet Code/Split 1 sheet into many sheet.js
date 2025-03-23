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
    var newSheet = ss.insertSheet('DataSet' + (i + 1));
    newSheet.getRange(1, 1, chunkData.length, chunkData[0].length).setValues(chunkData);
    newSheet.getRange(1, 1, chunkColors.length, chunkColors[0].length).setBackgrounds(chunkColors);
  }
}
