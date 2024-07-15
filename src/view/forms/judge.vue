<!--
 * @ Author: WouRaoyu
 * @ Create Time: 2024-07-09 16:45:29
 * @ Modified by: WouRaoyu
 * @ Modified time: 2024-07-15 14:16:05
 * @ Description:
 -->

<template>
    <van-pull-refresh v-model="loading" @refresh="onRefresh">
        <van-tabs style="margin-bottom: 64px;" v-model:active="active" scrollspy sticky>
            <van-tab title="基础信息">
                <van-cell-group inset>
                    <van-cell title="工程名称" :value=info.project />
                    <van-cell title="施工里程" :value=info.mileage />
                    <van-cell title="开挖宽度" :value="info.width + 'm'" />
                    <van-cell title="开挖高度" :value="info.height + 'm'" />
                    <van-cell title="开挖方式" :value=info.excavation />
                    <van-cell title="岩石类型" :value=info.lithology />
                </van-cell-group>
            </van-tab>

            <van-tab title="综合结论">
                <van-cell-group inset>
                    <van-cell value-class="left-span">
                        {{ info.conclusion }}
                    </van-cell>
                </van-cell-group>
            </van-tab>
            <van-tab title="围岩等级">
                <van-cell-group inset>
                    <van-cell title-class="title-limit">
                        <template #title>
                            <van-text-ellipsis :content="info.rockLevelDesc" expand-text="展开" collapse-text="收起" />
                        </template>
                        <van-tag v-if="info.rockLevel == 0" color="#19f519">Ⅰ级围岩</van-tag>
                        <van-tag v-if="info.rockLevel == 1" color="#7de17d">Ⅱ级围岩</van-tag>
                        <van-tag v-if="info.rockLevel == 2" color="#a5f5f5">Ⅲ级围岩</van-tag>
                        <van-tag v-if="info.rockLevel == 3" color="#e18719">Ⅳ级围岩</van-tag>
                        <van-tag v-if="info.rockLevel == 4" color="#a537f5">Ⅴ级围岩</van-tag>
                        <van-tag v-if="info.rockLevel == 5" color="#9b9b9b">Ⅵ级围岩</van-tag>
                    </van-cell>
                    <van-image width="100%" :src="'http://192.168.3.23:8000/' + info.rockLevelImg" />
                </van-cell-group>
            </van-tab>

            <van-tab title="坚硬程度">
                <van-cell-group inset>
                    <van-cell title-class="title-limit">
                        <template #title>
                            <van-text-ellipsis :content="info.hardnessDesc" expand-text="展开" collapse-text="收起" />
                        </template>
                        <van-tag v-if="info.hardness == 0" color="rgb(80, 60, 0)">极硬岩</van-tag>
                        <van-tag v-if="info.hardness == 1" color="rgb(190, 145, 0)">硬岩</van-tag>
                        <van-tag v-if="info.hardness == 2" color="rgb(255, 215, 100)">较软岩</van-tag>
                        <van-tag v-if="info.hardness == 3" color="rgb(255, 230, 150)">软岩</van-tag>
                        <van-tag v-if="info.hardness == 4" color="rgb(255, 245, 200)">极软岩</van-tag>
                    </van-cell>
                    <van-image width="100%" :src="'http://192.168.3.23:8000/' + info.hardnessImg" />
                </van-cell-group>
            </van-tab>

            <van-tab title="破碎程度">
                <van-cell-group inset>
                    <van-cell title-class="title-limit">
                        <template #title>
                            <van-text-ellipsis :content="info.fragmentDesc" expand-text="展开" collapse-text="收起" />
                        </template>
                        <van-tag v-if="info.fragment == 0" color="rgb(188, 230, 230)">完整</van-tag>
                        <van-tag v-if="info.fragment == 1" color="rgb(100, 193, 193)">较完整</van-tag>
                        <van-tag v-if="info.fragment == 2" color="rgb(88, 162, 162)">较破碎</van-tag>
                        <van-tag v-if="info.fragment == 3" color="rgb(69, 125, 125)">破碎</van-tag>
                        <van-tag v-if="info.fragment == 4" color="rgb(0, 65, 65)">极破碎</van-tag>
                    </van-cell>
                    <van-image width="100%" :src="'http://192.168.3.23:8000/' + info.fragmentImg" />
                </van-cell-group>
            </van-tab>
            <van-tab title="富水程度">
                <van-cell-group inset>
                    <van-cell title-class="title-limit">
                        <template #title>
                            <van-text-ellipsis :content="info.wateryDesc" expand-text="展开" collapse-text="收起" />
                        </template>
                        <van-tag v-if="info.watery == 0" color="rgb(220, 235, 250)">干燥</van-tag>
                        <van-tag v-if="info.watery == 1" color="rgb(142, 178, 241)">较干燥</van-tag>
                        <van-tag v-if="info.watery == 2" color="rgb(44, 108, 175)">较富水</van-tag>
                        <van-tag v-if="info.watery == 3" color="rgb(0, 71, 147)">富水</van-tag>
                        <van-tag v-if="info.watery == 4" color="rgb(0, 15, 75)">极富水</van-tag>
                    </van-cell>
                    <van-image width="100%" :src="'http://192.168.3.23:8000/' + info.wateryImg" />
                </van-cell-group>
            </van-tab>
            <van-tab title="地应力状态">
                <van-cell-group inset>
                    <van-cell title-class="title-limit">
                        <template #title>
                            <van-text-ellipsis :content="info.geostressDesc" expand-text="展开" collapse-text="收起" />
                        </template>
                        <van-tag v-if="info.geostress == 0" color="rgb(235, 215, 215)">无影响</van-tag>
                        <van-tag v-if="info.geostress == 1" color="rgb(245, 185, 125)">高地应力</van-tag>
                        <van-tag v-if="info.geostress == 2" color="rgb(255, 125, 25)">极高地应力</van-tag>
                    </van-cell>
                    <van-image width="100%" :src="'http://192.168.3.23:8000/' + info.geostressImg" />
                </van-cell-group>
            </van-tab>
        </van-tabs>
    </van-pull-refresh>
</template>


<script>
import axios from 'axios'
import { showSuccessToast, showFailToast } from 'vant';
import { ref } from 'vue';

export default {
    setup() {
        const active = ref(0);
        const dtId = ref('');
        const info = ref({});
        const loading = ref(false);

        const onRefresh = (first) => {
            axios.get('http://192.168.3.23:8000/judge_detail/' + dtId.value, { timeout: 5000 })
                .then(response => {
                    if (!first) {
                        showSuccessToast('刷新成功');
                    }
                    loading.value = false;
                    info.value = response.data;
                })
                .catch(function () {
                    showFailToast('连接服务失败');
                });
        };

        return {
            active,
            dtId,
            info,
            loading,
            onRefresh
        };
    },

    created() {
        this.dtId = this.$route.query.id;
        this.onRefresh(true);
    }
};
</script>

<style>
:root {
    --van-cell-group-inset-padding: var(--van-padding-md)
}

.title-limit {
    min-width: 80%;
}

.value-limit {
    min-width: 15%;
}

.left-span {
    display: block;
    width: 100%;
    text-align: left;
}
</style>