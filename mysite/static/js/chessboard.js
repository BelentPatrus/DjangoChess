class Chessboard {
  constructor() {
    this.elements = document.getElementsByClassName("chess-cell"); //chessboard logic
    this.chessboardFE = document.querySelector(".chessboard"); // UI
    this.gameStateId = -1;
  }

  // renders new board for html
  async renderBoardREST() {
    // HERE IS THE TRIGGER POINT FOR CHANNEL
    //RESTful get board
    var url = "http://127.0.0.1:8000/chess/latestBoard/" + this.gameStateId;
    const response = await fetch(url);
    const data = await response.json();
    this.sendBoardToOpponent(data);
    this.processBoard(data, false);
  }
  sendBoardToOpponent(data) {
     playerGameSocket.send(
       JSON.stringify({
         gamedata: data,
       })
     );
  }

  processBoard(data, freshBoardFlag = true) {
    //POINT OF ATTACK
    let jsonBoardData = JSON.parse(data.chessboard).replace(/\//g, "");
    this.gameStateId = freshBoardFlag
      ? (this.gameStateId = JSON.parse(data.gameState))
      : (this.gameStateId = data["gameState"]);
    this.chessboardFE.setAttribute("id", this.gameStateId.toString());

    for (const [i, element] of Array.from(this.elements).entries()) {
      while (element.firstChild) {
        element.removeChild(element.firstChild);
      }
      let pieceToRender = jsonBoardData[i];
      let type = FENKEY[pieceToRender].type.toLowerCase();
      let team = FENKEY[pieceToRender].team.toLowerCase();

      if (type in PIECEMAP) {
        const txt = document.createTextNode(PIECEMAP[type][team]);
        const div = document.createElement("Div");
        div.appendChild(txt);
        div.id = element.id;
        element.appendChild(div);
      }
    }
  }

  movesetHighlighter(highlightCords) {
    /* 
                args: list of cordinates in 2d array
                action: removes previous highlighting and adds highlight css to the args
            */
    this.removeHighlight();
    highlightCords.forEach((item) => {
      var id = item[0] + "-" + item[1];
      var cell = document.getElementById(id);
      cell.classList.add("highlight-move");
    });
  }
  removeHighlight() {
    /*
                action: removes all highlighting on the board
            */
    var highlightElements = document.querySelectorAll(".highlight-move");
    highlightElements.forEach((cell) => {
      cell.classList.remove("highlight-move");
    });
  }

  // chess board clicked
  async chessBoardClicked(clicks) {
    /*
                args: userClicks Global Array
                Deals with the clicking events in python and based on that result does an operation:
                    - highlighing cells
                    - moves a chess piece
            */
    var url = processClickUrl;

    const obj = {
      cords: JSON.stringify(clicks),
      gameState: this.gameStateId.toString(),
    };
    try {
      let response = await fetch(url, {
        method: "POST",
        headers: {
          "Content-type": "application/json",
          "X-CSRFToken": token,
        },
        body: JSON.stringify(obj),
      });
      let data = await response.json();
      console.table(data);
      if (data["sameTeam"]) {
        clicks[0] = clicks[1];
        clicks.splice(1, 1);
        this.chessBoardClicked(clicks);
      } else if (data["Operation"] === "highlight") {
        this.movesetHighlighter(data["moveSet"]);
      } else if (data["Operation"] === "move") {
        this.removeHighlight();
        await this.renderBoardREST();
        clicks = [];
      }
      console.log(
        "End of click event handler | userClicks: " + clicks + " Data: " + data
      );
    } catch (err) {
      console.error(`Error: ${err.message}\nStack trace:\n${err.stack}`);
    }
    return clicks;
  }
}

//display chess peice location (div id)
// var myFunction = function (btn) {
//   //chessboard logic
//   console.log(btn.currentTarget.id);
// };

// for (var i = 0; i < elements.length; i++) {
//   elements[i].addEventListener("click", myFunction, false);
// }

// helper function for render board

// start operations when new game is created
