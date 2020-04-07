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
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": "hello\n"
    }
   ],
   "source": [
    "print(\"hello\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": "1\n4\n9\n16\n25\n"
    }
   ],
   "source": [
    "def square(num):\n",
    "    return num**2\n",
    "my_nums = [1,2,3,4,5]\n",
    "for items in map(square, my_nums):\n",
    "    print(items)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "output_type": "error",
     "ename": "SyntaxError",
     "evalue": "unexpected EOF while parsing (<ipython-input-17-148591e0fc98>, line 7)",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-17-148591e0fc98>\"\u001b[1;36m, line \u001b[1;32m7\u001b[0m\n\u001b[1;33m    list(map(splicer,upper.names)\u001b[0m\n\u001b[1;37m                                 ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m unexpected EOF while parsing\n"
     ]
    }
   ],
   "source": [
    "def splicer(mystring):\n",
    "    if len(mystring)%2 == 0:\n",
    "        return \"EVEN\"\n",
    "    else:\n",
    "        return mystring[0]\n",
    "names = [\"mark\",\"Rae\",\"joe\"]\n",
    "list(map(splicer,names)"
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