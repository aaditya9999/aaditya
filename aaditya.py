{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "##Importing important libraries---\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Data is successfully imported\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Hours</th>\n",
       "      <th>Scores</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2.5</td>\n",
       "      <td>21</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>5.1</td>\n",
       "      <td>47</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3.2</td>\n",
       "      <td>27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>8.5</td>\n",
       "      <td>75</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>3.5</td>\n",
       "      <td>30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>1.5</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>9.2</td>\n",
       "      <td>88</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>5.5</td>\n",
       "      <td>60</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>8.3</td>\n",
       "      <td>81</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>2.7</td>\n",
       "      <td>25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>7.7</td>\n",
       "      <td>85</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>5.9</td>\n",
       "      <td>62</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>4.5</td>\n",
       "      <td>41</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>3.3</td>\n",
       "      <td>42</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>1.1</td>\n",
       "      <td>17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>8.9</td>\n",
       "      <td>95</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>2.5</td>\n",
       "      <td>30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>1.9</td>\n",
       "      <td>24</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>6.1</td>\n",
       "      <td>67</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>7.4</td>\n",
       "      <td>69</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>2.7</td>\n",
       "      <td>30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>4.8</td>\n",
       "      <td>54</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>3.8</td>\n",
       "      <td>35</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>6.9</td>\n",
       "      <td>76</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>7.8</td>\n",
       "      <td>86</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Hours  Scores\n",
       "0     2.5      21\n",
       "1     5.1      47\n",
       "2     3.2      27\n",
       "3     8.5      75\n",
       "4     3.5      30\n",
       "5     1.5      20\n",
       "6     9.2      88\n",
       "7     5.5      60\n",
       "8     8.3      81\n",
       "9     2.7      25\n",
       "10    7.7      85\n",
       "11    5.9      62\n",
       "12    4.5      41\n",
       "13    3.3      42\n",
       "14    1.1      17\n",
       "15    8.9      95\n",
       "16    2.5      30\n",
       "17    1.9      24\n",
       "18    6.1      67\n",
       "19    7.4      69\n",
       "20    2.7      30\n",
       "21    4.8      54\n",
       "22    3.8      35\n",
       "23    6.9      76\n",
       "24    7.8      86"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "path =  \"http://bit.ly/w-data\"\n",
    "Data = pd.read_csv(path)\n",
    "print(\"Data is successfully imported\")\n",
    "Data\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Hours</th>\n",
       "      <th>Scores</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2.5</td>\n",
       "      <td>21</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>5.1</td>\n",
       "      <td>47</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3.2</td>\n",
       "      <td>27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>8.5</td>\n",
       "      <td>75</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>3.5</td>\n",
       "      <td>30</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Hours  Scores\n",
       "0    2.5      21\n",
       "1    5.1      47\n",
       "2    3.2      27\n",
       "3    8.5      75\n",
       "4    3.5      30"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Hours</th>\n",
       "      <th>Scores</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>2.7</td>\n",
       "      <td>30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>4.8</td>\n",
       "      <td>54</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>3.8</td>\n",
       "      <td>35</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>6.9</td>\n",
       "      <td>76</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>7.8</td>\n",
       "      <td>86</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Hours  Scores\n",
       "20    2.7      30\n",
       "21    4.8      54\n",
       "22    3.8      35\n",
       "23    6.9      76\n",
       "24    7.8      86"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Data.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Hours</th>\n",
       "      <th>Scores</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>25.000000</td>\n",
       "      <td>25.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>5.012000</td>\n",
       "      <td>51.480000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>2.525094</td>\n",
       "      <td>25.286887</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.100000</td>\n",
       "      <td>17.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>2.700000</td>\n",
       "      <td>30.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>4.800000</td>\n",
       "      <td>47.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>7.400000</td>\n",
       "      <td>75.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>9.200000</td>\n",
       "      <td>95.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           Hours     Scores\n",
       "count  25.000000  25.000000\n",
       "mean    5.012000  51.480000\n",
       "std     2.525094  25.286887\n",
       "min     1.100000  17.000000\n",
       "25%     2.700000  30.000000\n",
       "50%     4.800000  47.000000\n",
       "75%     7.400000  75.000000\n",
       "max     9.200000  95.000000"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Data.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 25 entries, 0 to 24\n",
      "Data columns (total 2 columns):\n",
      " #   Column  Non-Null Count  Dtype  \n",
      "---  ------  --------------  -----  \n",
      " 0   Hours   25 non-null     float64\n",
      " 1   Scores  25 non-null     int64  \n",
      "dtypes: float64(1), int64(1)\n",
      "memory usage: 528.0 bytes\n"
     ]
    }
   ],
   "source": [
    "Data.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXAAAAD4CAYAAAD1jb0+AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8vihELAAAACXBIWXMAAAsTAAALEwEAmpwYAAAKs0lEQVR4nO3dX4jl91nH8c9jtqW2MXWHTMKaFLdCqEpBKoNUC70wFqSKyU0hFy1LCeTGP60IEr1JetcLKXohwtJWViyVkhYSpKhhbRFBQidJwaarpFSarl2TqUZTvVCDjxd7Sjfb2Z0zf87MPrOvFwzn/H7nnPk9C8Ob337Pv+ruADDPDxz1AADsjYADDCXgAEMJOMBQAg4w1InDPNjtt9/ep0+fPsxDAoz39NNPf7u716/ef6gBP336dDY3Nw/zkADjVdU3tttvCQVgKAEHGErAAYYScIChBBxgKAEHGErAAYYScIChDvWNPMDxUlW7fozvIDg4Ag7s2bViXFVCfQgsoQAMJeAAQwk4wFACDjCUgAMMJeAAQwk4wFACDjCUgAMMJeAAQwk4wFACDjCUgAMMJeAAQwk4wFACDjCUgAMMJeAAQwk4wFACDjCUgAMMJeAAQwk4wFACDjCUgAMMJeAAQwk4wFBLBbyqfrOqnquqr1TVp6vqDVW1VlVPVtXzi8uTqx4WgO/ZMeBVdVeS30iy0d1vT3JLkgeSPJzkfHffk+T8YhuAQ7LsEsqJJD9YVSeSvDHJt5Lcl+Tc4vZzSe4/8OkAuKYdA97d/5zk95K8kORSkv/o7r9Kcmd3X1rc51KSO7Z7fFU9VFWbVbW5tbV1cJMD3OSWWUI5mctn229N8iNJ3lRV71/2AN19trs3untjfX1975MC8BrLLKH8QpJ/6u6t7v7fJJ9L8nNJXqyqU0myuHxpdWMCcLVlAv5CkndW1RurqpLcm+RCkieSnFnc50ySx1czIgDbObHTHbr7qap6LMkzSV5N8mySs0luTfKZqnowlyP/vlUOCsBr7RjwJOnuR5I8ctXu/87ls3EAjoB3YgIMJeAAQwk4wFACDjCUgAPXtba2lqra1U+SXT9mbW3tiP+l8yz1KhTg5vXyyy+nu1d+nO+Gn+U5AwcYSsABhhJwgKEEHGAoAQcYSsABhhJwgKEEHGAoAQcYSsABhhJwgKEEHGAoAQcYSsABhhJwgKEEHGAoAQcYSsABhhJwgKEEHGAoAQcYSsABhhJwgKEEHGAoAQcYSsABhhJwgKGWCnhV/XBVPVZV/1BVF6rqZ6tqraqerKrnF5cnVz0sAN+z7Bn4HyT5i+7+8SQ/leRCkoeTnO/ue5KcX2wDcEh2DHhV3Zbk3Uk+kSTd/T/d/e9J7ktybnG3c0nuX82IAGxnmTPwH0uyleSPq+rZqvp4Vb0pyZ3dfSlJFpd3bPfgqnqoqjaranNra+vABge42S0T8BNJfjrJH3X3O5L8V3axXNLdZ7t7o7s31tfX9zgmAFdbJuAXk1zs7qcW24/lctBfrKpTSbK4fGk1IwKwnR0D3t3/kuSbVfW2xa57k3w1yRNJziz2nUny+EomBGBbJ5a8368n+VRVvT7J15N8MJfj/5mqejDJC0net5oRAdjOUgHv7i8n2djmpnsPdBoAluadmABDCTjAUAIOMJSAAwwl4ABDCTjAUAIOMJSAAwwl4ABDCTjAUAIOMJSAAwwl4ABDCTjAUAIOMJSAAwwl4ABDCTjAUAIOMJSAAwwl4ABDLfWt9MDNqx+5LXn0zYdzHHZFwIHrqo+8ku5e/XGq0o+u/DDHiiUUgKEEHGAoAQcYSsABhhJwgKEEHGAoAQcYSsABhhJwgKEEHGCopQNeVbdU1bNV9eeL7bWqerKqnl9cnlzdmABcbTdn4B9KcuGK7YeTnO/ue5KcX2wDcEiWCnhV3Z3kl5J8/Ird9yU5t7h+Lsn9BzoZANe17Bn47yf57ST/d8W+O7v7UpIsLu/Y7oFV9VBVbVbV5tbW1n5mBeAKOwa8qn45yUvd/fReDtDdZ7t7o7s31tfX9/IrANjGMp8H/q4kv1JV703yhiS3VdWfJnmxqk5196WqOpXkpVUOCsBr7XgG3t2/0913d/fpJA8k+evufn+SJ5KcWdztTJLHVzYlAN9nP68D/2iS91TV80nes9gG4JDs6ivVuvuLSb64uP6vSe49+JEAWIZ3YgIMJeAAQwk4wFACDjCUgAMMJeAAQwk4wFACDjCUgAMMJeAAQwk4wFACDjCUgAMMJeAAQwk4wFC7+jxw4OZUVSs/xsmTJ1d+jONGwIHr6u5dP6aq9vQ4dscSCsBQAg4wlIADDCXgAEMJOMBQAg4wlIADDCXgAEMJOMBQAg4wlIADDCXgAEMJOMBQAg4wlIADDCXgAEPtGPCqektVfaGqLlTVc1X1ocX+tap6sqqeX1z6Og2AQ7TMGfirSX6ru38iyTuT/GpV/WSSh5Oc7+57kpxfbANwSHYMeHdf6u5nFte/k+RCkruS3Jfk3OJu55Lcv6IZAdjGrtbAq+p0knckeSrJnd19Kbkc+SR3XOMxD1XVZlVtbm1t7XNcAL5r6YBX1a1JPpvkw939yrKP6+6z3b3R3Rvr6+t7mRGAbSwV8Kp6XS7H+1Pd/bnF7her6tTi9lNJXlrNiABsZ5lXoVSSTyS50N0fu+KmJ5KcWVw/k+Txgx8PgGs5scR93pXkA0n+vqq+vNj3u0k+muQzVfVgkheSvG8lEwKwrR0D3t1/m6SucfO9BzsOAMta5gwcYFuXV1h3d1t3r2qcm46AA3smxkfLZ6EADCXgAEMJOMBQAg4wlIADDCXgAEMJOMBQAg4wlIADDCXgAEMJOMBQAg4wlIADDCXgAEMJOMBQPg/8Bne9D8y/Hp/TDMefgN/grhfiqhJquIlZQgEYSsABhhLwG8Ta2lqqalc/SXZ1/7W1tSP+VwIHyRr4DeLll19e+Xr2Xp8QBW5MzsABhhJwgKEEHGAoa+A3iH7ktuTRN6/+GMCxIeA3iPrIK4fyJGY/utJDAIfIEgrAUAIOMJSAAwxlDfwGsuo32pw8eXKlvx84XAJ+g9jLE5g+jRBubvtaQqmqX6yqf6yqr1XVwwc1FAA72/MZeFXdkuQPk7wnycUkX6qqJ7r7qwc1HDsvq1zrdmfmcPztZwnlZ5J8rbu/niRV9WdJ7ksi4AdIiIFr2c8Syl1JvnnF9sXFvteoqoeqarOqNre2tvZxOACutJ+Ab/d/9+87Xezus9290d0b6+vr+zgcAFfaT8AvJnnLFdt3J/nW/sYBYFn7CfiXktxTVW+tqtcneSDJEwczFgA72fOTmN39alX9WpK/THJLkk9293MHNhkA17WvN/J09+eTfP6AZgFgF3wWCsBQAg4wVB3mG0WqaivJNw7tgMff7Um+fdRDwDb8bR6sH+3u73sd9qEGnINVVZvdvXHUc8DV/G0eDksoAEMJOMBQAj7b2aMeAK7B3+YhsAYOMJQzcIChBBxgKAEfqKo+WVUvVdVXjnoWuFJVvaWqvlBVF6rquar60FHPdJxZAx+oqt6d5D+T/El3v/2o54HvqqpTSU519zNV9UNJnk5yv69aXA1n4AN1998k+bejngOu1t2XuvuZxfXvJLmQbb6pi4Mh4MBKVNXpJO9I8tQRj3JsCThw4Krq1iSfTfLh7n7lqOc5rgQcOFBV9bpcjvenuvtzRz3PcSbgwIGpqkryiSQXuvtjRz3PcSfgA1XVp5P8XZK3VdXFqnrwqGeChXcl+UCSn6+qLy9+3nvUQx1XXkYIMJQzcIChBBxgKAEHGErAAYYScIChBBxgKAEHGOr/Ad1fNKkE+E66AAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.boxplot(Data)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.xlabel('Hours',fontsize=15)\n",
    "plt.ylabel('Scores',fontsize=15)\n",
    "plt.title('Hours studied vs Score', fontsize=10)\n",
    "plt.scatter(Data.Hours,Data.Scores,color='blue',marker='*')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[2.5],\n",
       "       [5.1],\n",
       "       [3.2],\n",
       "       [8.5],\n",
       "       [3.5],\n",
       "       [1.5],\n",
       "       [9.2],\n",
       "       [5.5],\n",
       "       [8.3],\n",
       "       [2.7],\n",
       "       [7.7],\n",
       "       [5.9],\n",
       "       [4.5],\n",
       "       [3.3],\n",
       "       [1.1],\n",
       "       [8.9],\n",
       "       [2.5],\n",
       "       [1.9],\n",
       "       [6.1],\n",
       "       [7.4],\n",
       "       [2.7],\n",
       "       [4.8],\n",
       "       [3.8],\n",
       "       [6.9],\n",
       "       [7.8]])"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X = Data.iloc[:,:-1].values\n",
    "Y = Data.iloc[:,1].values\n",
    "X"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([21, 47, 27, 75, 30, 20, 88, 60, 81, 25, 85, 62, 41, 42, 17, 95, 30,\n",
       "       24, 67, 69, 30, 54, 35, 76, 86], dtype=int64)"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "X_train,X_test,Y_train,Y_test = train_test_split(X,Y,random_state = 0,test_size=0.2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "X train.shape = (20, 1)\n",
      "Y train.shape = (20,)\n",
      "X test.shape  = (5, 1)\n",
      "Y test.shape  = (5,)\n"
     ]
    }
   ],
   "source": [
    "print(\"X train.shape =\", X_train.shape)\n",
    "print(\"Y train.shape =\", Y_train.shape)\n",
    "print(\"X test.shape  =\", X_test.shape)\n",
    "print(\"Y test.shape  =\", Y_test.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LinearRegression\n",
    "linreg=LinearRegression()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Training our algorithm is finished\n"
     ]
    }
   ],
   "source": [
    "linreg.fit(X_train,Y_train)\n",
    "print(\"Training our algorithm is finished\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "B0 = 2.018160041434683 \n",
      "B1 = [9.91065648]\n"
     ]
    }
   ],
   "source": [
    "print(\"B0 =\",linreg.intercept_,\"\\nB1 =\",linreg.coef_)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "Y0 = linreg.intercept_ + linreg.coef_*X_train"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.scatter(X_train,Y_train,color='green',marker='+')\n",
    "plt.plot(X_train,Y0,color='orange')\n",
    "plt.xlabel(\"Hours\",fontsize=15)\n",
    "plt.ylabel(\"Scores\",fontsize=15)\n",
    "plt.title(\"Regression line(Train set)\",fontsize=10)\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[16.88414476 33.73226078 75.357018   26.79480124 60.49103328]\n"
     ]
    }
   ],
   "source": [
    "Y_pred=linreg.predict(X_test)\n",
    "print(Y_pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([20, 27, 69, 30, 62], dtype=int64)"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Y_test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.plot(X_test,Y_pred,color='red')\n",
    "plt.scatter(X_test,Y_test,color='black',marker='+')\n",
    "plt.xlabel(\"Hours\",fontsize=15)\n",
    "plt.ylabel(\"Scores\",fontsize=15)\n",
    "plt.title(\"Regression line(Test set)\",fontsize=10)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Actual</th>\n",
       "      <th>Result</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>20</td>\n",
       "      <td>16.884145</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>27</td>\n",
       "      <td>33.732261</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>69</td>\n",
       "      <td>75.357018</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>30</td>\n",
       "      <td>26.794801</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>62</td>\n",
       "      <td>60.491033</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Actual     Result\n",
       "0      20  16.884145\n",
       "1      27  33.732261\n",
       "2      69  75.357018\n",
       "3      30  26.794801\n",
       "4      62  60.491033"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Y_test1 = list(Y_test)\n",
    "prediction=list(Y_pred)\n",
    "df_compare = pd.DataFrame({ 'Actual':Y_test1,'Result':prediction})\n",
    "df_compare"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9454906892105356"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn import metrics\n",
    "metrics.r2_score(Y_test,Y_pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import mean_squared_error,mean_absolute_error"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean Squared Error      =  21.5987693072174\n",
      "Root Mean Squared Error =  4.6474476121003665\n",
      "Mean Absolute Error     =  4.6474476121003665\n"
     ]
    }
   ],
   "source": [
    "MSE = metrics.mean_squared_error(Y_test,Y_pred)\n",
    "root_E = np.sqrt(metrics.mean_squared_error(Y_test,Y_pred))\n",
    "Abs_E = np.sqrt(metrics.mean_squared_error(Y_test,Y_pred))\n",
    "print(\"Mean Squared Error      = \",MSE)\n",
    "print(\"Root Mean Squared Error = \",root_E)\n",
    "print(\"Mean Absolute Error     = \",Abs_E)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "predicted score for a student studying 9.25 hours : [93.69173249]\n"
     ]
    }
   ],
   "source": [
    "Prediction_score = linreg.predict([[9.25]])\n",
    "print(\"predicted score for a student studying 9.25 hours :\",Prediction_score)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
