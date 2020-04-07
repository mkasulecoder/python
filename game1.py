{
 "nbformat": 4,
 "nbformat_minor": 2,
 "metadata": {
  "language_info": {
   "name": "python",
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "version": "3.8.1-final"
  },
  "orig_nbformat": 2,
  "file_extension": ".py",
  "mimetype": "text/x-python",
  "name": "python",
  "npconvert_exporter": "python",
  "pygments_lexer": "ipython3",
  "version": 3,
  "kernelspec": {
   "name": "python38132bitaf07833046bb4389b6e713fe3b6d4a07",
   "display_name": "Python 3.8.1 32-bit"
  }
 },
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": "X|O|X\nO|X|O\nX|O|X\n"
    }
   ],
   "source": [
    "from IPython.display import clear_output\n",
    "def display_board(board):\n",
    "    clear_output() # helps clear boardan d not make reapeated boaard\n",
    "    print(board[7]+\"|\"+board[8]+\"|\"+board[9])\n",
    "    print(board[4]+\"|\"+board[5]+\"|\"+board[6])\n",
    "    print(board[1]+\"|\"+board[2]+\"|\"+board[3])\n",
    "test_board = [\"#\", \"X\", \"O\", \"X\", \"O\", \"X\", \"O\", \"X\", \"O\", \"X\" ]\n",
    "display_board(test_board)\n",
    ""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "output_type": "error",
     "ename": "SyntaxError",
     "evalue": "'return' outside function (<ipython-input-6-af6bed493c78>, line 6)",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-6-af6bed493c78>\"\u001b[1;36m, line \u001b[1;32m6\u001b[0m\n\u001b[1;33m    return (\"X\", \"O\")\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m 'return' outside function\n"
     ]
    }
   ],
   "source": [
    "#ask players gor input.\n",
    "marker = \"\"\n",
    "while marker != \"X\" and marker != \"O\":\n",
    "    marker = input(\"Player1: Choose X or O: \").upper()\n",
    "if marker == \"X\":\n",
    "    return (\"X\", \"O\")\n",
    "else:\n",
    "    return (\"O\", \"X\")\n",
    ""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ]
}