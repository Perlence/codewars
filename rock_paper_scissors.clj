(ns rock-paper-scissors
  (:require [clojure.test :refer :all]))

(defn rps [p1 p2]
  (cond (= p1 p2) "Draw!"
        (= p1 "rock") (if (= p2 "scissors") "Player 1 won!" "Player 2 won!")
        (= p1 "paper") (if (= p2 "rock") "Player 1 won!" "Player 2 won!")
        (= p1 "scissors") (if (= p2 "paper") "Player 1 won!" "Player 2 won!")))

(deftest rps-tests
  (testing "player 1 win"
    (are [p1 p2] (= "Player 1 won!" (rps p1 p2))
      "rock" "scissors"
      "scissors" "paper"
      "paper" "rock"))
  (testing "player 2 win"
    (are [p1 p2] (= "Player 2 won!" (rps p1 p2))
      "scissors" "rock"
      "paper" "scissors"
      "rock" "paper"))
  (testing "draw"
    (are [p1 p2] (= "Draw!" (rps p1 p2))
      "rock" "rock"
      "scissors" "scissors"
      "paper" "paper")))
