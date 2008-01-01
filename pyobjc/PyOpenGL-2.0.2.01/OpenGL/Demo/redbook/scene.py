#!

# This is statement is required by the build system to query build info
if __name__ == '__build__':
	raise Exception

'''
scene.c from the Redbook examples.  
Converted to Python by Jason Petrone(jp@demonseed.net) 8/00

/*
 * Copyright (c) 1993-1997, Silicon Graphics, Inc.
 * ALL RIGHTS RESERVED 
 * Permission to use, copy, modify, and distribute this software for 
 * any purpose and without fee is hereby granted, provided that the above
 * copyright notice appear in all copies and that both the copyright notice
 * and this permission notice appear in supporting documentation, and that 
 * the name of Silicon Graphics, Inc. not be used in advertising
 * or publicity pertaining to distribution of the software without specific,
 * written prior permission. 
 *
 * THE MATERIAL EMBODIED ON THIS SOFTWARE IS PROVIDED TO YOU "AS-IS"
 * AND WITHOUT WARRANTY OF ANY KIND, EXPRESS, IMPLIED OR OTHERWISE,
 * INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF MERCHANTABILITY OR
 * FITNESS FOR A PARTICULAR PURPOSE.  IN NO EVENT SHALL SILICON
 * GRAPHICS, INC.  BE LIABLE TO YOU OR ANYONE ELSE FOR ANY DIRECT,
 * SPECIAL, INCIDENTAL, INDIRECT OR CONSEQUENTIAL DAMAGES OF ANY
 * KIND, OR ANY DAMAGES WHATSOEVER, INCLUDING WITHOUT LIMITATION,
 * LOSS OF PROFIT, LOSS OF USE, SAVINGS OR REVENUE, OR THE CLAIMS OF
 * THIRD PARTIES, WHETHER OR NOT SILICON GRAPHICS, INC.  HAS BEEN
 * ADVISED OF THE POSSIBILITY OF SUCH LOSS, HOWEVER CAUSED AND ON
 * ANY THEORY OF LIABILITY, ARISING OUT OF OR IN CONNECTION WITH THE
 * POSSESSION, USE OR PERFORMANCE OF THIS SOFTWARE.
 * 
 * US Government Users Restricted Rights 
 * Use, duplication, or disclosure by the Government is subject to
 * restrictions set forth in FAR 52.227.19(c)(2) or subparagraph
 * (c)(1)(ii) of the Rights in Technical Data and Computer Software
 * clause at DFARS 252.227-7013 and/or in similar or successor
 * clauses in the FAR or the DOD or NASA FAR Supplement.
 * Unpublished-- rights reserved under the copyright laws of the
 * United States.  Contractor/manufacturer is Silicon Graphics,
 * Inc., 2011 N.  Shoreline Blvd., Mountain View, CA 94039-7311.
 *
 * OpenGL(R) is a registered trademark of Silicon Graphics, Inc.
 */

/*
 *  scene.c
 *  This program demonstrates the use of the GL lighting model.
 *  Objects are drawn using a grey material characteristic. 
 *  A single light source illuminates the objects.
 */

'''

import sys

try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
except:
  print '''
ERROR: PyOpenGL not installed properly.  
        '''
  sys.exit()


#  Initialize material property and light source.
def init():
   light_ambient =  [0.0, 0.0, 0.0, 1.0]
   light_diffuse =  [1.0, 1.0, 1.0, 1.0]
   light_specular =  [1.0, 1.0, 1.0, 1.0]
#  light_position is NOT default value
   light_position =  [1.0, 1.0, 1.0, 0.0]

   glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
   glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
   glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
   glLightfv(GL_LIGHT0, GL_POSITION, light_position)
   
   glEnable(GL_LIGHTING)
   glEnable(GL_LIGHT0)
   glEnable(GL_DEPTH_TEST)


def display():
   glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
   glPushMatrix()
   glRotatef(20.0, 1.0, 0.0, 0.0)
   glPushMatrix()
   glTranslatef(-0.75, 0.5, 0.0); 
   glRotatef(90.0, 1.0, 0.0, 0.0)
   glutSolidTorus(0.275, 0.85, 15, 15)
   glPopMatrix()

   glPushMatrix()
   glTranslatef(-0.75, -0.5, 0.0); 
   glRotatef (270.0, 1.0, 0.0, 0.0)
   glutSolidCone(1.0, 2.0, 15, 15)
   glPopMatrix()

   glPushMatrix()
   glTranslatef(0.75, 0.0, -1.0)
   glutSolidSphere(1.0, 15, 15)
   glPopMatrix()

   glPopMatrix()
   glFlush()


def reshape(w, h):
   glViewport(0, 0, w, h)
   glMatrixMode (GL_PROJECTION)
   glLoadIdentity()
   if w <= h:
      glOrtho(-2.5, 2.5, -2.5*h/w, 
               2.5*h/w, -10.0, 10.0)
   else: 
      glOrtho(-2.5*w/h, 
               2.5*w/h, -2.5, 2.5, -10.0, 10.0)
   glMatrixMode(GL_MODELVIEW)
   glLoadIdentity()


def keyboard(key, x, y):
   if key == chr(27):
       sys.exit(0)
   


#  Main Loop
#  Open window with initial window size, title bar, 
#  RGBA display mode, and handle input events.

glutInit(sys.argv)
glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize (500, 500)
glutCreateWindow('scene')
init()
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard)
glutDisplayFunc(display)
glutMainLoop()
