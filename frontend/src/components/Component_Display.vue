<!-- src/components -->
<script setup lang="ts">
  import Shipment_Component from '@/components/Shipment_Component.vue';
  import Process_Component from '@/components/Process_Component.vue';
  import Order_Component from '@/components/Order_Component.vue';
  import Resource_Component from '@/components/Resource_Component.vue';
</script>

<template>
  <div class="component-frame">
    <div class="component-choice-frame">
      <h3 class="component-name">Shipments</h3>
      <div class="component-menu-frame">
        <h6>choose view</h6>
        <ul class="component-menu">
          <li><button class="scroll-button">Resources</button></li>
          <li><button class="scroll-button">Shipments</button></li>
          <li><button class="scroll-button">Processes</button></li>
          <li><button class="scroll-button">Orders</button></li>
        </ul>
      </div>
    </div>
    <Shipment_Component/>
  </div>
</template>

<style>
  .component-choice-frame {
    display: flex;
    border: 2px solid #555;
    box-sizing: border-box;
    height: 3rem;
  }

  .component-name {
    flex: 2 1 0;
    box-sizing: border-box;
    line-height: 0.6;
  }

  .component-menu-frame {
    flex: 1 1 0;
    border: 2px solid #555;
    box-sizing: border-box;
  }

  .component-menu-frame h6{
    line-height: 0;
  }

  .component-menu {
    display: inline-block;
    top: calc(50% + .25rem);      
    left: 0;
    max-height: 160px;             
    overflow-y: auto;              
    background:#333;
    padding:2px 2px;
    margin: 0;
    list-style:none;
    box-shadow:0 8px 18px rgba(0,0,0,.5);

    opacity: 0;
    transform: translateY(-8px);
    visibility: hidden;
    transition: opacity .25s ease, transform .25s ease;
  }

  .component-menu-frame:hover .component-menu {
    opacity: 1;
    transform: translateY(0);
    visibility: visible;
  }
    
  .scroll-button {
    display:block;
    padding:0 1rem;
    text-decoration:none;
    color:#36499f;
    font-size:.9rem;
    width: 100%
  }
</style>