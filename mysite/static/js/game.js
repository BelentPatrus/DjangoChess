class Game {
  constructor(Chessboard) {
    this.userClicks = [];
    this.chessboard = Chessboard;
  }

  isPiece(cellDiv) {
    /*
                args: chess cell.
                return: true or false, chess piece cell or empty.
            */
    const childDiv = cellDiv.firstElementChild;
    if (childDiv.hasAttribute("id")) return true;
    return false;
  }
  async startGame() {
    // game logic
    var url = "http://127.0.0.1:8000/chess/getData/";
    const response = await fetch(url);
    const data = await response.json();
    this.chessboard.processBoard(data);
  }

  async setupEventListener(event) {
    // chessboard logic
    if (event.target.closest(".chess-cell")) {
      let cellID = event.target.id.split("-");
      cellID[0] = parseInt(cellID[0]);
      cellID[1] = parseInt(cellID[1]);
      // Clicked same piece as before
      if (
        this.userClicks.length == 1 &&
        cellID[0] === this.userClicks[0][0] &&
        cellID[1] === this.userClicks[0][1]
      ) {
        console.log(
          "Clicked same piece as before userClicks: " +
            this.userClicks +
            " eventClick: " +
            cellID
        );
        return;
      }
      this.userClicks.push(cellID);
      //Check if only a empty cell was clicked
      let testID = document.getElementById(event.target.id);
      if (this.userClicks.length == 1 && !this.isPiece(testID)) {
        this.userClicks = [];
        return;
      }
      this.userClicks = await this.chessboard.chessBoardClicked(
        this.userClicks
      );
    }
  }
}
