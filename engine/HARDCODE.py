﻿#c2="If you’ve been doing all of the work assigned so far, you may have noticed something. In many of the problems, you were asked to find the speed of an object (or, if the direction was obvious, its velocity) after it moved from some initial position to a final position. The solution strategy you employed over and over again was to solve the equations of motion, solve for the time, substitute the time, find the speed or velocity. We used this in the very first example in the book and the first actual homework problem to show that a mass dropped from rest that falls a height H hits the ground at speed v = √2gH, but later we discovered that a mass that slides down a frictionless inclined plane starting from rest a height H above the ground arrives at the ground as a speed √2gH independent of the slope of the incline! If you were mathematically inclined – or used a different textbook, one with a separate section on the kinematics of constant acceleration motion (a subject this textbook has assiduously avoided, instead requiring you to actually solve the equations of motion using calculus repeatedly and then use algebra as needed to answer the questions) you might have noted that you can actually do the algebra associated with this elimination of time once and for all for a constant acceleration problem in one dimension. It is simple. If you look back at week 1, you can see if that if you integrate a constant acceleration of an object twice, you obtain: v(t) = at + v0 x(t) = 1 2 at2 + v0t + x0 as a completely general kinematic solution in one dimension, where v0 is the initial speed and x0 is the initial x position at time t = 0. Now, suppose you want to find the speed v1 the object will have when it reaches position x1. One can algebraically, once and for all note that this must occur at some time t1 such that: v(t1) = at1 + v0 = v1 x(t1) = 1 2 at21 + v0t1 + x0 = x1 We can algebraically solve the first equation once and for all for t1: t1 = v1 − v0 a (238) 144 Week 3: Work and Energy and substitute the result into the second equation, elminating time altogether from the solutions: 1 2 a  v1 − v0 a 2 + v0  v1 − v0 a  + x0 = x1 1 2a 􀀀 v2 1 − 2v0v1 + v2 0  +  v0v1 − v2 0 a  = x1 − x0 v2 1 − 2v0v1 + v2 0 + 2v0v1 − 2v2 0 = 2a(x1 − x0) or v2 1 − v2 0 = 2a(x1 − x0) (239) Many textbooks encourage students to memorize this equation as well as the two kinematic solutions for constant acceleration very early – often before one has even learned Newton’s Laws – so that students never have to actually learn why these solutions are important or where they come from, but at this point you’ve hopefully learned both of those things well and it is time to make solving problems of this kinds a little bit easier. However, we will not do so using this constant acceleration kinematic equation even now! There is no need! As we will see below, it is quite simple to eliminate time from Newton’s Second Law itself once and for all, and obtain a powerful way of solving many, many physics problems – in particular, ones where the questions asked do not depend on specific times – without the tedium of integrating out the equations of motion. This “time independent” formulation of force laws and motion turns out, in the end, to be even more general and useful than Newton’s Laws themselves, surviving the transition to quantum theory where the concepts of force and acceleration do not. One very good thing about waiting as we have done and not memorizing anything, let alone kinematic constant acceleration solutions, is that this new formulation in terms of work and energy works just fine for non-constant forces and accelerations, where the kinematic solutions above are (as by now you should fully appreciate, having worked through e.g. the drag force and investigated the force exerted by springs, neither of which are constant in space or in time) completely useless and wrong. Let us therefore begin now with this relatively meaningless kinematical result that arises from eliminating time for a constant acceleration in one dimension only – planning to use it only long enough to ensure that we never have to use it because we’ve found something even better that is far more meaningful : v2 1 − v2 0 = 2ax (240) where x is the displacement of the object x1 − x0. If we multiply by m (the mass of the object) and move the annoying 2 over to the other side, we can make the constant acceleration a into a constant force Fx = ma: (ma)x = 1 2 mv2 1 − 1 2 mv2 0 (241) Fxx = 1 2 mv2 1 − 1 2 mv2 0 (242) We now define the work done by the constant force Fx on the mass m as it moves through the distance x to be: W = Fxx. (243) The work can be positive or negative. Of course, not all forces are constant. We have to wonder, then, if this result or concept is as fragile as the integral of a constant acceleration (which does not “work”, so to speak, for springs!) or if it can handle springs, pendulums, real gravity (not near the Earth’s surface) and so on. As you might guess, the answer is yes – we wouldn’t have bothered introducing and naming the concept if Week 3: Work and Energy 145 all we cared about was constant acceleration problems as we already had a satisfactory solution for them – but before we turn this initial result into a theorem that follows directly from the axiom of Newton’s Second Law made independent of time, we should discuss units of work, energy, and all that. 3.1.1: Units of Work and Energy Work is a form of energy. As always when we first use a new named quantity in physics, we need to define its units so we can e.g. check algebraic results for kinematic consistency, correctly identify work, and learn to quantitatively appreciated it when people refer to quantities in other sciences or circumstances (such as the energy yield of a chemical reaction, the power consumed by an electric light bulb, or the energy consumed and utilized by the human body in a day) in these units. In general, the definition of SI units can most easily be remembered and understood from the basic equations that define the quantity of interest, and the units of energy are no exception. Since work is defined above to be a force times a distance, the SI units of energy must be the SI units of force (Newtons) times the SI units of length (meters). The units themselves are named (as many are) after a Famous Physicist, James Prescott Joule80 . Thus: 1 Joule = 1 Newton-meter = 1 kilogram-meter2 second2 (244) 3.1.2: Kinetic Energy The latter, we also note, are the natural units of mass times speed squared. We observe that this is the quantity that changes when we do work on a mass, and that this energy appears to be a characteristic of the moving mass associated with the motion itself (dependent only on the speed v). We therefore define the quantity changed by the work to be the kinetic energy81 and will use the symbol K to represent it in this work: K = 1 2 mv2 (245) Note that kinetic energy is a relative quantity – it depends upon the inertial frame in which it is measured. Suppose we consider the kinetic energy of a block of mass m sliding forward at a constant speed vb in a railroad car travelling at a constant speed vc. The frame of the car is an inertial reference frame and so Newton’s Laws must be valid there. In particular, our definition of kinetic energy that followed from a solution to Newton’s Laws ought to be valid there. It should be equally valid on the ground, but these two quantities are not equal. Relative to the ground, the speed of the block is: vg = vb + vc (246) and the kinetic energy of the block is: Kg = 1 2 mv2 g = 1 2 mv2 b + 1 2 mv2 c + mvbvc (247) 80Wikipedia: http://www.wikipedia.org/wiki/James Prescott Joule. He worked with temperature and heat and was one of the first humans on Earth to formulate and initially experimentally verify the Law of Conservation of Energy, discussed below. He also discovered and quantified resistive electrical heating (Joule heating) and did highly precise experiments that showed that mechanical energy delivered into a closed system increased its temperature is the work converted into heat. 81The work “kinetic” means “related to the motion of material bodies”, although we also apply it to e.g. hyperkinetic people... 146 Week 3: Work and Energy or Kg = Kb + 1 2 mv2 c + mvbvc (248) where Kb is the kinetic energy of the block in the frame of the train. Worse, the train is riding on the Earth, which is not exactly at rest relative to the sun, so we could describe the velocity of the block by adding the velocity of the Earth to that of the train and the block within the train. The kinetic energy in this case is so large that the difference in the energy of the block due to its relative motion in the train coordinates is almost invisible against the huge energy it has in an inertial frame in which the sun is approximately at rest. Finally, as we discussed last week, the sun itself is moving relative to the galactic center or the “rest frame of the visible Universe”. What, then, is the actual kinetic energy of the block? I don’t know that there is such a thing. But the kinetic energy of the block in the inertial reference frame of any well-posed problem is 1 2mv2, and that will have to be enough for us. As we will prove below, this definition makes the work done by the forces of nature consistent within the frame, so that our computations will give us answers consistent with experiment and experience in the frame coordinates"
c2="""What happens to the energy added to or removed from an object (that is really made up of many
particles bound together by internal e.g. molecular forces) by things like my non-conservative hand
as I give a block treated as a “particle” a push, or non-conservative kinetic friction and drag forces
as they act on the block to slow it down as it slides along a table? This is not a trivial question.
To properly answer it we have to descend all the way into the conceptual abyss of treating every
single particle that makes up the system we call “the block” and every single particle that makes
up the system consisting of “everything else in the Universe but the block” and all of the internal
forces between them – which happen, as far as we can tell, to be strictly conservative forces – and
then somehow average over them to recover the ability to treat the block like a particle, the table
like a fixed, immovable object it slides on, and friction like a comparatively simple force that does
non-conservative work on the block.
It requires us to invent things like statistical mechanics to do the averaging, thermodynamics to
describe certain kinds of averaged systems, and whole new sciences such as chemistry and biology
that use averaged energy concepts with their own fairly stable rules that cannot easily be connected
back to the microscopic interactions that bind quarks and electrons into atoms and atoms together
into molecules. It’s easy to get lost in this, because it is both fascinating and really difficult.
I’m therefore going to give you a very important empirical law (that we can understand well
enough from our treatment of particles so far) and a rather heuristic description of the connections
between microscopic interactions and energy and the macroscopic mechanical energy of things like
blocks, or cars, or human bodies.
The important empirical law is the Law of Conservation of Energy86. Whenever we examine
a physical system and try very hard to keep track of all of the mechanical energy exchanges withing
that system and between the system and its surroundings, we find that we can always account for
them all without any gain or loss. In other words, we find that the total mechanical energy of an
isolated system never changes, and if we add or remove mechanical energy to/from the system, it
has to come from or go to somewhere outside of the system. This result, applied to well defined
systems of particles, can be formulated as the First Law of Thermodynamics:
Qin = Eof +Wby (325)
In words, the heat energy flowing in to a system equals the change in the internal total mechanical
energy of the system plus the external work (if any) done by the system on its surroundings. The
total mechanical energy of the system itself is just the sum of the potential and kinetic energies of
all of its internal parts and is simple enough to understand if not to compute. The work done by
the system on its surroundings is similarly simple enough to understand if not to compute. The
hard part of this law is the definition of heat energy, and sadly, I’m not going to give you more than
the crudest idea of it right now and make some statements that aren’t strictly true because to treat
heat correctly requires a major chunk of a whole new textbook on textbfThermodynamics. So take
the following with a grain of salt, so to speak.
When a block slides down a rough table from some initial velocity to rest, kinetic friction turns
the bulk organized kinetic energy of the collectively moving mass into disorganized microscopic
energy – heat. As the rough microscopic surfaces bounce off of one another and form and break
chemical bonds, it sets the actual molecules of the block bounding, increasing the internal microscopic
mechanical energy of the block and warming it up. Some of it similarly increasing the internal
microscopic mechanical energy of the table it slide across, warming it up. Some of it appears as
light energy (electromagnetic radiation) or sound energy – initially organized energy forms that
themselves become ever more disorganized. Eventually, the initial organized energy of the block
becomes a tiny increase in the average internal mechanical energy of a very, very large number of
objects both inside and outside of the original system that we call the block, a process we call being"""