import numpy as np

VERY_STRICT = False

class ReflectError(Exception):
	def __init__(self, normal, velocity):
		self.normal = normal
		self.velocity = velocity

	def __str__(self):
		return "\n !! \n !! ball [{}, {}] seems to be coming from inside the object [{}, {}].\n !!".format(self.velocity[0], self.velocity[1], self.normal[0], self.normal[1])

class ContactError(Exception):
	def __init__(self, restitution):
		self.restitution = restitution

	def __str__(self):
		return "\n !! \n !! Incorrect coeff. of restitution {}.\n !!".format(self.restitution)

class Ball(object):
	def __init__(self, initpos, initvel, radius, world):
		self.world = world
		self._pos = np.array(initpos, dtype=np.float64)
		self.radius = int(radius)
		self._velocity = np.array(initvel, dtype=np.float64)

		self.RESTITUTION = world.RESTITUTION
		if self.RESTITUTION > 1.0 or self.RESTITUTION < 0:
			raise ContactError(self.RESTITUTION)

	@property
	def pos(self):
		return list(self._pos)

	@pos.setter
	def pos(position_container):
		self._pos = np.array(position_container)

	@property
	def velocity(self):
		return list(self._velocity)

	def update(self):
		self.handle_collisions()
		self._pos += self._velocity / self.world.fps
		#print(self._velocity/self.world.fps)

	def reflect(self, normals, restitution=None):
		"""
		returns new velocity of the ball
		"""
		# use default restitution if not specified
		restitution = self.RESTITUTION
		if restitution > 1.0 or restitution < 0:
			raise ContactError(restitution)

		# determine the true normal.
		normal = np.array([0.0, 0.0])
		for n in normals:
			normal += n / np.linalg.norm(n)
		if np.linalg.norm(normal) < 1e-4:
			normal -= random.choice(normals)
		along_normal = normal.dot(self._velocity)/np.linalg.norm(normal)**2 * normal
		across_normal = self._velocity - along_normal

		if normal.dot(self._velocity) > 0:
			if VERY_STRICT:
				raise ReflectError(normal, self._velocity)
			result = self._velocity
		else:
			result = along_normal * -restitution + across_normal
		self._velocity = result
		return list(result)

	def handle_collisions(self):
		normals = list()
		flag = self.hit_boundary(normals)
		if flag == True:
			self.reflect(normals)
		# Similarily, the following:
		# self.hit_brick()
		# self.hit_paddle()

	def hit_boundary(self, normals):
		# You need to imagine an envelope around all objects in the world.
		# Else contacts will be detected too late.
		# 
		# What if object crosses more than 1 boundaries in a particular iteration?
		# Just add the NORMALIZED normals. return NORMALIZED sum!!
		# If this normal is too "small", then remove any one of the normals, from the sum
		# 
		# So, all detectors need to store the "surface penetration amounts" in the container provided
		hit = False
		if self.pos[0] > self.world.w - self.radius:
			# right wall
			hit = True
			normals.append([-1, 0])
			# self.pos[0] + self.radius - self.world.w
		if self.pos[0] < self.radius:
			# left wall
			hit = True
			normals.append([1, 0])
			# self.radius - self.pos[0]
		if self.pos[1] < self.radius:
			# top wall
			hit = True
			normals.append([0, 1])
			# self.radius - self.pos[1]
		if self.pos[1] > self.world.h - self.radius:
			# bottom wall
			hit = True
			normals.append([0, -1])
			# self.pos[0] + self.radius - self.world.h
		if hit:
			print(normals)
		return hit

	# def hit_paddle(self, normals):
	# 	pass

	# def hit_brick(self, normals):
	# 	pass

class Brick(object):
	COLORS = [(0, 0, 0), (0, 255, 0), (255, 0, 0), (0, 0, 255)]
	def __init__(self, grid_loc, tag, world):
		self.w, self.h = self.world.brick_shape
		self.grid_loc = grid_loc
		self.pos = self.transform_to_px()
		self.tag = tag

	def transform_to_px(self):
		return self.world.padding

	def update(self, delta):
		self.tag += delta
		if self.tag	== -1:
			self.world.gc.append()

if __name__ == '__main__':

	world = {'width'       : 400,
			 'height'      : 400 * 9 / 16,
			 'restitution' : 1,
			 'radius'      : 8,
			 'aspect'      : 16.0/9,
			 'fps'         : 30,
			 'brick_shape' : (24, 9),
			 'padding'     : (18, 30)}

	class boo(object):
		def __init__(self, layout, config):
			self.radius = config['radius']
			self.brick_shape = config['brick_shape']
			self.aspect = config['aspect']
			self.w = config['width']
			self.h = int(self.w / self.aspect)
			self.fps = config['fps']
			self.RESTITUTION = config['restitution']
	
	world = boo("dsd", world)
	b = Ball((200, 150), (2.4, -1.2), 8, world)
	normal = np.array([0.4, 0.3])
	print(b.reflect(normal, 1))