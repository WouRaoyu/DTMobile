<!--
 * @ Author: WouRaoyu
 * @ Create Time: 2024-07-09 16:44:34
 * @ Modified by: WouRaoyu
 * @ Modified time: 2024-07-14 17:25:43
 * @ Description:
 -->

<template>
    <van-pull-refresh v-model="refreshing" @refresh="onRefresh">
        <van-list v-model:loading="loading" :finished="finished" finished-text="没有更多了" @load="onLoad">
            <van-cell-group inset v-for="item in list" :key="item" @click="toItem(item.dtId)">
                <van-cell :title="item.project + item.mileage" :label=item.conclusion>
                    <van-tag v-if="item.rockLevel == 0" color="#19f519">Ⅰ级围岩</van-tag>
                    <van-tag v-if="item.rockLevel == 1" color="#7de17d">Ⅱ级围岩</van-tag>
                    <van-tag v-if="item.rockLevel == 2" color="#a5f5f5">Ⅲ级围岩</van-tag>
                    <van-tag v-if="item.rockLevel == 3" color="#e18719">Ⅳ级围岩</van-tag>
                    <van-tag v-if="item.rockLevel == 4" color="#a537f5">Ⅴ级围岩</van-tag>
                    <van-tag v-if="item.rockLevel == 5" color="#9b9b9b">Ⅵ级围岩</van-tag>
                </van-cell>
            </van-cell-group>
        </van-list>
    </van-pull-refresh>
</template>

<script>
import axios from 'axios'
import { Toast } from 'vant';
import { ref } from 'vue';

export default {
    setup() {
        const list = ref([]);
        const loading = ref(false);
        const finished = ref(false);
        const refreshing = ref(false);

        const onLoad = () => {
            axios.get('http://localhost:8000/judge_list/', { timeout: 5000 })
                .then(response => {
                    if (refreshing.value) {
                        list.value = [];
                        refreshing.value = false;
                    }
                    loading.value = false;
                    finished.value = true;
                    list.value = response.data;
                })
                .catch(function () {
                    Toast.fail('连接服务失败');
                    loading.value = false;
                    finished.value = true;
                });
        };

        const onRefresh = () => {
            // 清空列表数据
            finished.value = false;

            // 重新加载数据 
            // 将 loading 设置为 true，表示处于加载状态
            loading.value = true;
            onLoad();
        };

        return {
            list,
            onLoad,
            loading,
            finished,
            onRefresh,
            refreshing,
        };
    },
    methods: {
        toItem(item) {
            this.$router.push({ path: '/judge', query: { id: item } });
        }
    }
};
</script>

<style>
:root {
    --van-cell-group-inset-padding: var(--van-padding-md)
}
</style>