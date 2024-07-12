<template>
    <van-grid square :column-num="2" :gutter="15">
        <van-grid-item replace to="/list-judge">
            <van-image width="8rem" height="8rem" src="icons/ProcessData.png" /> 综合研判报告
        </van-grid-item>
        <van-grid-item replace to="/voxel">
            <van-image width="8rem" height="8rem" src="icons/TSAnalysis.png" /> 三维地质环境
        </van-grid-item>
        <van-grid-item replace to="/list-tsp">
            <van-image width="8rem" height="8rem" src="icons/MSData.png" /> 物探-地震波法
        </van-grid-item>
        <van-grid-item replace to="/list-tem">
            <van-image width="8rem" height="8rem" src="icons/MSData.png" /> 物探-瞬变电磁法
        </van-grid-item>
        <van-grid-item replace to="/list-gpr">
            <van-image width="8rem" height="8rem" src="icons/MSData.png" /> 物探-地质雷达法
        </van-grid-item>
        <van-grid-item replace to="/list-ahd">
            <van-image width="8rem" height="8rem" src="icons/MSData.png" /> 钻探-超前水平钻
        </van-grid-item>
        <van-grid-item replace to="/list-dbh">
            <van-image width="8rem" height="8rem" src="icons/MSData.png" /> 钻探-加深炮孔
        </van-grid-item>
        <van-grid-item replace to="/list-tfs">
            <van-image width="8rem" height="8rem" src="icons/MSData.png" /> 掌子面地质素描
        </van-grid-item>
    </van-grid>
</template>

<script>
import { Grid, GridItem } from 'vant';

export default {
    components: {
        [Grid.name]: Grid,
        [GridItem.name]: GridItem
    },

    data() {
        return {
        };
    },

    computed: {
    },

    methods: {
    }
};
</script>