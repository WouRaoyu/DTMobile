import { createRouter, createWebHashHistory } from 'vue-router';

const routes = [
  {
    name: 'notFound',
    path: '/:path(.*)+',
    redirect: {
      name: 'home',
    },
  },
  {
    name: 'home',
    path: '/home',
    component: () => import('./view/home'),
    meta: {
      title: '主页',
    },
  },
  {
    name: 'voxel',
    path: '/voxel',
    component: () => import('./view/voxel'),
    meta: {
      title: '视图',
    },
  },
  {
    name: 'list-tfs',
    path: '/list-tfs',
    component: () => import('./view/lists/tfs'),
    meta: {
      title: '掌子面地质素描',
    },
  },
  {
    name: 'list-dbh',
    path: '/list-dbh',
    component: () => import('./view/lists/dbh'),
    meta: {
      title: '加深炮孔',
    },
  },
  {
    name: 'list-ahd',
    path: '/list-ahd',
    component: () => import('./view/lists/ahd'),
    meta: {
      title: '超前水平钻',
    },
  },
  {
    name: 'list-gpr',
    path: '/list-gpr',
    component: () => import('./view/lists/gpr'),
    meta: {
      title: '地质雷达物探',
    },
  },
  {
    name: 'list-tem',
    path: '/list-tem',
    component: () => import('./view/lists/tem'),
    meta: {
      title: '瞬变电磁',
    },
  },
  {
    name: 'list-tsp',
    path: '/list-tsp',
    component: () => import('./view/lists/tsp'),
    meta: {
      title: '地震波物探',
    },
  },
  {
    name: 'list-judge',
    path: '/list-judge',
    component: () => import('./view/lists/judge'),
    meta: {
      title: '综合研判',
    },
  },
  {
    name: 'judge',
    path: '/judge',
    component: () => import('./view/forms/judge'),
    meta: {
      title: '综合研判',
    },
  }
];

const router = createRouter({
  routes,
  history: createWebHashHistory(),
});

router.beforeEach((to, from, next) => {
  const title = to.meta && to.meta.title;
  if (title) {
    document.title = title;
  }
  next();
});

export { router };
