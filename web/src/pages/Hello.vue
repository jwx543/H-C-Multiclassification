<template>
    <div class="hello-pos">
        <el-form ref="form" :model="form" label-width="80px" size="mini">
            <el-form-item label="导航栏位置">
                <el-select v-model="form.position" placeholder="请选择导航栏位置">
                    <el-option label="上" value=0></el-option>
                    <el-option label="偏上" value=1></el-option>
                    <el-option label="左" value=2></el-option>
                    <el-option label="偏左" value=3></el-option>
                    <el-option label="右" value=4></el-option>
                    <el-option label="偏右" value=5></el-option>
                </el-select>
            </el-form-item>
            <el-form-item label="tag数量">
                <el-input v-model="form.num"></el-input>
            </el-form-item>
            <el-form-item label="背景颜色">
                <el-input v-model="form.bcgcolors"></el-input>
            </el-form-item>
            <el-form-item label="字体颜色">
                <el-input v-model="form.fontcolors"></el-input>
            </el-form-item>
            <el-form-item label="导航栏水平位置">
                <el-select v-model="form.horzpos" placeholder="请选择导航栏水平位置">
                    <el-option label="上" value=0></el-option>
                    <el-option label="中" value=1></el-option>
                    <el-option label="右" value=2></el-option>
                </el-select>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="onSubmit">立即查询</el-button>
            </el-form-item>
            <el-form-item label="评分">
                <el-input type="textarea" v-model="form.scores"></el-input>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
import {HttpManager} from "../api";

export default {
    data() {
        return {
            form: {
                position: '',
                num: '',
                numint: 0,
                bcgcolors: '',
                bcgint: 2,
                fontcolors: '',
                fontint: 2,
                horzpos: '',
                scores: ''
            }
        }
    },
    methods: {
        onSubmit() {
            this.str2int()

            let jdata = {
                'position': this.form.position,
                'nums': this.form.numint,
                'bagcol': this.form.bcgint,
                'fontcol': this.form.fontint,
                'hposition': this.form.horzpos
            }

            HttpManager.getScores(jdata).then(res => {
                this.form.scores = res
            })
        },
        str2int(){
            this.form.numint = parseInt(this.form.num)

            if(this.form.bcgcolors === '白色' || this.form.bcgcolors === '粉色'){
                this.form.bcgint = 0
            }else if(this.form.bcgcolors === '黑色' || this.form.bcgcolors === '棕色'){
                this.form.bcgint = 1
            }else if(this.form.bcgcolors === '蓝色'){
                this.form.bcgint = 2
            }else if(this.form.bcgcolors === '灰色'){
                this.form.bcgint = 3
            }else{
                this.form.bcgint = 4
            }

            if(this.form.fontcolors === '白色' || this.form.fontcolors === '粉色'){
                this.form.fontint = 0
            }else if(this.form.fontcolors === '黑色' || this.form.fontcolors === '棕色'){
                this.form.fontint = 1
            }else if(this.form.fontcolors === '蓝色'){
                this.form.fontint = 2
            }else if(this.form.fontcolors === '灰色'){
                this.form.fontint = 3
            }else{
                this.form.fontint = 4
            }

        }
    }
}
</script>

<style scoped>
.hello-wrap {
    position: relative;
    background: #241e0b fixed center;
    background-size: cover;
    width: 100%;
    height: 100%;
}

.hello-pos {
    position: absolute;
    left: 50%;
    top: 35%;
    width: 300px;
    height: 380px;
    margin: -150px 0 0 -190px;
    padding: 40px;
    border-radius: 5px;
    background: #e3e3e3;
}
</style>