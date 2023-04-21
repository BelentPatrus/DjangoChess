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
