'use client';                     // 👈  obligatorio

import { Canvas } from '@react-three/fiber';
import { OrbitControls, useGLTF } from '@react-three/drei';
import { Suspense } from 'react';

function Scene() {
  const { scene } = useGLTF('/assets/scene.glb');
  return <primitive object={scene} dispose={null} />;
}

export default function Stage3d(props) {   // 👈  DEFAULT EXPORT
  return (
    <Canvas frameloop="demand"
            camera={{ position: [0, 2, 6], fov: 45 }}
            {...props}>
      <Suspense fallback={null}>
        <Scene />
      </Suspense>
      <OrbitControls enableZoom={false} />
    </Canvas>
  );
}


