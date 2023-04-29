const PIECE = {
  P: "♙",
  R: "♖",
  N: "♘",
  B: "♗",
  Q: "♕",
  K: "♔",
  p: "♟",
  r: "♜",
  n: "♞",
  b: "♝",
  q: "♛",
  k: "♚",
};
const PIECEMAP = {
  rook: { white: PIECE.R, black: PIECE.r },
  bishop: { white: PIECE.B, black: PIECE.b },
  knight: { white: PIECE.N, black: PIECE.n },
  queen: { white: PIECE.Q, black: PIECE.q },
  king: { white: PIECE.K, black: PIECE.k },
  pawn: { white: PIECE.P, black: PIECE.p },
};

const FENKEY = {
  P: { type: "pawn", team: "white" },
  R: { type: "rook", team: "white" },
  N: { type: "knight", team: "white" },
  B: { type: "bishop", team: "white" },
  Q: { type: "queen", team: "white" },
  K: { type: "king", team: "white" },
  p: { type: "pawn", team: "black" },
  r: { type: "rook", team: "black" },
  n: { type: "knight", team: "black" },
  b: { type: "bishop", team: "black" },
  q: { type: "queen", team: "black" },
  k: { type: "king", team: "black" },
  1: { type: "empty", team: "empty" },
};
