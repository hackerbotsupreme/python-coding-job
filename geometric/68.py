Deleting points from Convex Hull

Difficulty Level : Medium
Last Updated : 17 Jan, 2023
Read
Discuss
Courses
Practice
Video
Given a fixed set of points. We need to find convex hull of given set. We also need to find convex hull when a point is removed from the set.

Example: 

Initial Set of Points: (-2, 8) (-1, 2) (0, 1) (1, 0)
                        (-3, 0) (-1, -9) (2, -6) (3, 0) 
                        (5, 3) (2, 5) 
Initial convex hull:- (-2, 8) (-3, 0) (-1, -9) (2, -6)
                      (5, 3)
Point to remove from the set : (-2, 8)
Final convex hull: (2, 5) (-3, 0) (-1, -9) (2, -6) (5, 3)
Recommended: Please try your approach on {IDE} first, before moving on to the solution.
Prerequisite : Convex Hull (Simple Divide and Conquer Algorithm)
The algorithm for solving the above problem is very easy. We simply check whether the point to be removed is a part of the convex hull. If it is, then we have to remove that point from the initial set and then make the convex hull again (refer Convex hull (divide and conquer) ). 

And if not then we already have the solution (the convex hull will not change). 

C++
// C++ program to demonstrate delete operation
// on Convex Hull.
#include<bits/stdc++.h>
using namespace std;
 
// stores the center of polygon (It is made
// global because it is used in compare function)
pair<int, int> mid;
 
// determines the quadrant of a point
// (used in compare())
int quad(pair<int, int> p)
{
    if (p.first >= 0 && p.second >= 0)
        return 1;
    if (p.first <= 0 && p.second >= 0)
        return 2;
    if (p.first <= 0 && p.second <= 0)
        return 3;
    return 4;
}
 
// Checks whether the line is crossing the polygon
int orientation(pair<int, int> a, pair<int, int> b,
                pair<int, int> c)
{
    int res = (b.second-a.second)*(c.first-b.first) -
              (c.second-b.second)*(b.first-a.first);
 
    if (res == 0)
        return 0;
    if (res > 0)
        return 1;
    return -1;
}
 
// compare function for sorting
bool compare(pair<int, int> p1, pair<int, int> q1)
{
    pair<int, int> p = make_pair(p1.first - mid.first,
                                 p1.second - mid.second);
    pair<int, int> q = make_pair(q1.first - mid.first,
                                 q1.second - mid.second);
 
    int one = quad(p);
    int two = quad(q);
 
    if (one != two)
        return (one < two);
    return (p.second*q.first < q.second*p.first);
}
 
// Finds upper tangent of two polygons 'a' and 'b'
// represented as two vectors.
vector<pair<int, int> > merger(vector<pair<int, int> > a,
                               vector<pair<int, int> > b)
{
    // n1 -> number of points in polygon a
    // n2 -> number of points in polygon b
    int n1 = a.size(), n2 = b.size();
 
    int ia = 0, ib = 0;
    for (int i=1; i<n1; i++)
        if (a[i].first > a[ia].first)
            ia = i;
 
    // ib -> leftmost point of b
    for (int i=1; i<n2; i++)
        if (b[i].first < b[ib].first)
            ib=i;
 
    // finding the upper tangent
    int inda = ia, indb = ib;
    bool done = 0;
    while (!done)
    {
        done = 1;
        while (orientation(b[indb], a[inda], a[(inda+1)%n1]) >=0)
            inda = (inda + 1) % n1;
 
        while (orientation(a[inda], b[indb], b[(n2+indb-1)%n2]) <=0)
        {
            indb = (n2+indb-1)%n2;
            done = 0;
        }
    }
 
    int uppera = inda, upperb = indb;
    inda = ia, indb=ib;
    done = 0;
    int g = 0;
    while (!done)//finding the lower tangent
    {
        done = 1;
        while (orientation(a[inda], b[indb], b[(indb+1)%n2])>=0)
            indb=(indb+1)%n2;
 
        while (orientation(b[indb], a[inda], a[(n1+inda-1)%n1])<=0)
        {
            inda=(n1+inda-1)%n1;
            done=0;
        }
    }
 
    int lowera = inda, lowerb = indb;
    vector<pair<int, int> > ret;
 
    //ret contains the convex hull after merging the two convex hulls
    //with the points sorted in anti-clockwise order
    int ind = uppera;
    ret.push_back(a[uppera]);
    while (ind != lowera)
    {
        ind = (ind+1)%n1;
        ret.push_back(a[ind]);
    }
 
    ind = lowerb;
    ret.push_back(b[lowerb]);
    while (ind != upperb)
    {
        ind = (ind+1)%n2;
        ret.push_back(b[ind]);
    }
    return ret;
 
}
 
// Brute force algorithm to find convex hull for a set
// of less than 6 points
vector<pair<int, int> > bruteHull(vector<pair<int, int> > a)
{
    // Take any pair of points from the set and check
    // whether it is the edge of the convex hull or not.
    // if all the remaining points are on the same side
    // of the line then the line is the edge of convex
    // hull otherwise not
    set<pair<int, int> >s;
 
    for (int i=0; i<a.size(); i++)
    {
        for (int j=i+1; j<a.size(); j++)
        {
            int x1 = a[i].first, x2 = a[j].first;
            int y1 = a[i].second, y2 = a[j].second;
 
            int a1 = y1-y2;
            int b1 = x2-x1;
            int c1 = x1*y2-y1*x2;
            int pos = 0, neg = 0;
            for (int k=0; k<a.size(); k++)
            {
                if (a1*a[k].first+b1*a[k].second+c1 <= 0)
                    neg++;
                if (a1*a[k].first+b1*a[k].second+c1 >= 0)
                    pos++;
            }
            if (pos == a.size() || neg == a.size())
            {
                s.insert(a[i]);
                s.insert(a[j]);
            }
        }
    }
 
    vector<pair<int, int> >ret;
    for (auto e : s)
        ret.push_back(e);
 
    // Sorting the points in the anti-clockwise order
    mid = {0, 0};
    int n = ret.size();
    for (int i=0; i<n; i++)
    {
        mid.first += ret[i].first;
        mid.second += ret[i].second;
        ret[i].first *= n;
        ret[i].second *= n;
    }
    sort(ret.begin(), ret.end(), compare);
    for (int i=0; i<n; i++)
        ret[i] = make_pair(ret[i].first/n, ret[i].second/n);
 
    return ret;
}
 
// Returns the convex hull for the given set of points
vector<pair<int, int>> findHull(vector<pair<int, int>> a)
{
    // If the number of points is less than 6 then the
    // function uses the brute algorithm to find the
    // convex hull
    if (a.size() <= 5)
        return bruteHull(a);
 
    // left contains the left half points
    // right contains the right half points
    vector<pair<int, int>>left, right;
    for (int i=0; i<a.size()/2; i++)
        left.push_back(a[i]);
    for (int i=a.size()/2; i<a.size(); i++)
        right.push_back(a[i]);
 
    // convex hull for the left and right sets
    vector<pair<int, int>>left_hull = findHull(left);
    vector<pair<int, int>>right_hull = findHull(right);
 
    // merging the convex hulls
    return merger(left_hull, right_hull);
}
 
// Returns the convex hull for the given set of points after
// removing a point p.
vector<pair<int, int>> removePoint(vector<pair<int, int>> a,
                                   vector<pair<int, int>> hull,
                                   pair<int, int> p)
{
    // checking whether the point is a part of the
    // convex hull or not.
    bool found = 0;
    for (int i=0; i < hull.size() && !found; i++)
        if (hull[i].first == p.first &&
                hull[i].second == p.second)
            found = 1;
 
    // If point is not part of convex hull
    if (found == 0)
        return hull;
 
    // if it is the part of the convex hull then
    // we remove the point and again make the convex hull
    // and if not, we print the same convex hull.
    for (int i=0; i<a.size(); i++)
    {
        if (a[i].first==p.first && a[i].second==p.second)
        {
            a.erase(a.begin()+i);
            break;
        }
    }
 
    sort(a.begin(), a.end());
    return findHull(a);
}
 
// Driver code
int main()
{
    vector<pair<int, int> > a;
    a.push_back(make_pair(0, 0));
    a.push_back(make_pair(1, -4));
    a.push_back(make_pair(-1, -5));
    a.push_back(make_pair(-5, -3));
    a.push_back(make_pair(-3, -1));
    a.push_back(make_pair(-1, -3));
    a.push_back(make_pair(-2, -2));
    a.push_back(make_pair(-1, -1));
    a.push_back(make_pair(-2, -1));
    a.push_back(make_pair(-1, 1));
 
    int n = a.size();
 
    // sorting the set of points according
    // to the x-coordinate
    sort(a.begin(), a.end());
    vector<pair<int, int> >hull = findHull(a);
 
    cout << "Convex hull:\n";
    for (auto e : hull)
        cout << e.first << " "
             << e.second << endl;
 
    pair<int, int> p = make_pair(-5, -3);
    removePoint(a, hull, p);
 
    cout << "\nModified Convex Hull:\n";
    for (auto e:hull)
        cout << e.first << " "
             << e.second << endl;
 
    return 0;
}
Output: 

convex hull:
-3 0
-1 -9
2 -6
5 3
2 5
Time Complexity: 
It is simple to see that the maximum time taken per query is the time taken to construct the convex hull which is O(n*logn). So, the overall complexity is O(q*n*logn), where q is the number of points to be deleted.

Auxiliary Space: O(n), since n extra space has been taken.



This article is contributed by Aarti_Rathi and Amritya Vagmi. If you like GeeksforGeeks and would like to contribute, you can also write an article using write.geeksforgeeks.org or mail your article to review-team@geeksforgeeks.org. See your article appearing on the GeeksforGeeks main page and help other Geeks.
Please write comments if you find anything incorrect, or you want to share more information about the topic discussed above.
 





Like
0
Previous
Dynamic Convex hull | Adding Points to an Existing Convex Hull
Next
Minimum area of a Polygon with three points given
Related Articles
1.
Dynamic Convex hull | Adding Points to an Existing Convex Hull
2.
Perimeter of Convex hull for a given set of points
3.
Convex Hull using Jarvis' Algorithm or Wrapping
4.
Convex Hull using Graham Scan
5.
Convex Hull using Divide and Conquer Algorithm
6.
Convex Hull | Monotone chain algorithm
7.
Quickhull Algorithm for Convex Hull
8.
Check if the given point lies inside given N points of a Convex Polygon
9.
Count of index pairs (i, j) such that string after deleting ith character is equal to string after deleting jth character
10.
Find maximum points which can be obtained by deleting elements from array
Article Contributed By :
https://media.geeksforgeeks.org/auth/avatar.png
GeeksforGeeks
Vote for difficulty
Current difficulty : Medium
Easy
Normal
Medium
Hard
Expert
Improved By :
khushboogoyal499
surinderdawra388
_shinchancode
rishav1329
ruhelaa48
Article Tags :
DSA
Geometric
Practice Tags :
Geometric